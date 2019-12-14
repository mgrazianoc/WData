from googleapiclient.discovery import build
from itertools import count
import time


def init_youtube_api():
    print("Initializing YouTube Api V3...")
    api_key = init_key()
    api = build("youtube", "v3", developerKey=api_key)
    return api


def init_key():
    print("Gathering user developer Key...")
    with open("config/Key.txt", 'r') as code:
        api_key = code.readline()
    return api_key

# ---------------------------------------------------------------------------------------------------------------------


def api_manager(parse):
    process = init_youtube_api()
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
    pass


# ---------------------------------------------------------------------------------------------------------------------

def get_most_popular(process, country_code, category):
    filters = "nextPageToken, " \
              "items(etag, id, " \
              "snippet(publishedAt, channelId, title, description, thumbnails/maxres/url, tags)," \
              "statistics)"

    print("Getting videos information from youtube...")
    request = process.videos().list(part="id, snippet, statistics",
                                    chart="mostPopular",
                                    regionCode=country_code,
                                    hl="pt_BR",
                                    videoCategoryId=category,
                                    maxResults=50,
                                    fields=filters)

    most_popular = [request.execute()]

    for i in count(0):
        print(f"Page {i + 1}...")
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

    print("Getting channels information...")

    # dictionary most_popular will have exactly 200 videos inside items, 50 each.
    # so the idea here is to go to each channels video and gather their information
    channel_info = []

    for i in range(4):
        for j in range(50):
            channel = most_popular[i]['items'][j]['snippet']['channelId']
            request = process.channels().list(part="id, snippet, contentDetails, statistics, topicDetails",
                                              id=f"{channel}",
                                              fields=filters
                                              )
            channel_info.append(request.execute())

    return channel_info


# ---------------------------------------------------------------------------------------------------------------------


def get_categories(process, country_code):
    request = process.videoCategories().list(part="id, snippet",
                                             regionCode=country_code
                                             )
    print("Getting categories information from youtube...")
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
    print(f"Download of Raw Data completed at {time.ctime(time.time())}")
    if data2 is None:
        return data1
    else:
        data = {"most_popular": data1, "channels_info": data2}
        return data
