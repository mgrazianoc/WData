from googleapiclient.discovery import build
from itertools import count
import time
import logging
import os


# setting up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatting = logging.Formatter(
    "%(name)s:%(asctime)s:%(levelname)s:%(message)s")

# creating specific file handler on g_logs
directory = os.getcwd()
file_handler = logging.FileHandler(f"{directory}/g_logs/youtube_api.log")
file_handler.setFormatter(formatting)
logger.addHandler(file_handler)

# creating stream handler, simple format
cmd_handler = logging.StreamHandler()
logger.addHandler(cmd_handler) 


# ---------------------------------------------------------------------------------------------------------------------


def init_youtube_api():
    logger.info("Initializing YouTube Api V3...")
    
    api_key = init_key()
    api = build("youtube", "v3", developerKey=api_key)
    return api


def init_key():
    logger.info("Gathering user developer Key...")
    
    with open("a_data_processing/YouTube/config/Key.txt", 'r') as code:
        api_key = code.readline()
    return api_key

# ---------------------------------------------------------------------------------------------------------------------


def api_manager(parse):
    process = init_youtube_api()

    try:
        logger.info("Initializing api_manager")
        
        if parse.task == "trends":
            most_popular = get_most_popular(process, parse.country, parse.category)
            current_time = time.ctime(time.time())
            most_popular.append(current_time)

            channel_info = get_channels_info(process, most_popular)

            raw_data = send_raw_data(most_popular, channel_info)

            return raw_data
        elif parse.task == "categories":
            raw_data = get_categories(process, parse.country)
            return raw_data
        elif parse.task == "single_channel":
            raw_data = get_single_channel_info(process, parse.id)  # id needs implementation
            return raw_data
        elif parse.task == "channels_from_category":
            raw_data = get_channels_from_category(process, parse.category)
            return raw_data
        else:
            print("Invalid input")
            return
    except AttributeError:
        if parse["task"] == "trends":
            most_popular = get_most_popular(process, parse["country"], parse["category"])
            current_time = time.ctime(time.time())
            most_popular.append(current_time)

            channel_info = get_channels_info(process, most_popular)

            raw_data = send_raw_data(most_popular, channel_info)
            return raw_data
        elif parse["task"] == "categories":
            raw_data = get_categories(process, parse["country"])
            return raw_data

# ---------------------------------------------------------------------------------------------------------------------


def get_most_popular(process, country_code, category):
    filters = "nextPageToken, " \
              "items(etag, id, " \
              "snippet(publishedAt, channelId, title, categoryId, description, thumbnails/maxres/url, tags)," \
              "statistics)"

    logger.info("Getting videos information from youtube...")
    request = process.videos().list(part="id, snippet, statistics",
                                    chart="mostPopular",
                                    regionCode=country_code,
                                    hl="pt_BR",
                                    videoCategoryId=category,
                                    maxResults=50,
                                    fields=filters)

    most_popular = [request.execute()]

    for i in count(0):
        logger.info(f"........Page {i + 1}")
        # When making requests, "nextPageToken" will eventually become "previousPageToken", i.e., it is the last page
        try:
            query = most_popular[i]["nextPageToken"]
        except KeyError:
            break

        request = process.videos().list(part="id, snippet, statistics",
                                        chart="mostPopular",
                                        regionCode=country_code,
                                        pageToken=query,
                                        hl="pt_BR",
                                        videoCategoryId=category,
                                        maxResults=50,
                                        fields=filters
                                        )
        data = request.execute()
        most_popular.append(data)

    return most_popular


def get_channels_info(process, most_popular):

    filters = "items(etag, id," \
              "snippet(title, description, publishedAt, country)," \
              "contentDetails/relatedPlaylists/uploads,"\
              "statistics(viewCount, subscriberCount, videoCount))"

    logger.info("Getting channels information...")

    # dictionary most_popular will have exactly 200 videos inside items, 50 each.
    # so the idea here is to go to each channels video and gather their information
    channel_info = []
    channel_number = 0

    for i in range(4):
        for j in range(50):
            logger.info(f"........Channel {channel_number + 1}")
            channel = most_popular[i]['items'][j]['snippet']['channelId']
            request = process.channels().list(part="id, snippet, contentDetails, statistics, topicDetails",
                                              id=f"{channel}",
                                              fields=filters
                                              )
            channel_info.append(request.execute())
            channel_number += 1

    return channel_info


# ---------------------------------------------------------------------------------------------------------------------


def get_categories(process, country_code):
    request = process.videoCategories().list(part="id, snippet",
                                             regionCode=country_code
                                             )
    logger.info("Getting categories information from youtube...")
    result = request.execute()
    send_raw_data(result)
    return 0


# ---------------------------------------------------------------------------------------------------------------------


def get_single_channel_info(process, code):
    print(process + code)
    return 0


# ---------------------------------------------------------------------------------------------------------------------


def get_channels_from_category(process, category):
    return process, category


def send_raw_data(data1, data2=None):
    logger.info(f"Download of Raw Data completed at {time.ctime(time.time())}")
    if data2 is None:
        return data1
    else:
        data = {"most_popular": data1, "channels_info": data2}
        return data
