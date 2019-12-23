import re
import itertools
import a_data_processing.YouTube.partial_web_scrapping
from a_data_processing.YouTube.config.constants import DICTIONARY_BR
from wdata_config.loggers import create_info_log as create_info_log



logger = create_info_log(__name__)


# ---------------------------------------------------------------------------------------------------------------------

def filter_manager(data, **kwargs):
    logger.info("Initiating filter_manager")
    if kwargs.get("task") == "trends":
        filtered_data = videos_filter(data)
        filtered_data = channel_filter(data, filtered_data)
        extra_data = a_data_processing.YouTube.partial_web_scrapping.web_scrapping_manager(filtered_data)
        extra_data = time_construct(extra_data)
        extra_data = id_construct(extra_data, **kwargs)
        final_data = create_dict(extra_data)
        final_data = string_correction(final_data)
        return final_data

# ---------------------------------------------------------------------------------------------------------------------


# This function will filter videos related data
def videos_filter(data):
    logger.info("Filtering videos data junk...")
    
    # constructing dictionary structure
    filtered_data = {"Data": []}
    filtered_data["Data"].append({})
    
    # labelling first position process. Using this because it was easy to work with it
    filtered_data["Data"][0].update({"Position": 1})
    
    # making the data more accessible
    data = data["most_popular"]
    
    # there are 4 lists of items to separate. Each items has a list of dictionaries
    
    time = data[4]
    
    for t in range(4):
        # we are gonna using try because the data from the API is irregular. I.E: don't have fixed values
        try:
            for i in itertools.count(0):
                for j, k in data[t]["items"][i].items():
                    # filtering process
                    if j == "etag":
                        filtered_data["Data"][i].update({"Video E-tag": k})  # insuring labeling "Video etag"
                        continue
                        
                    if j == "id":
                        filtered_data["Data"][i].update({"Video ID": k})  # insuring labeling "Video Id"
                        continue
                    
                    if j == "snippet":
                        for m, n in data[t]["items"][i][j].items():
                            if m == "publishedAt":
                                filtered_data["Data"][i].update({"Publication Date": n[:10]})
                                filtered_data["Data"][i].update({"Publication Time": n[11:19]})
                            if m == "thumbnails":
                                url = data[t]["items"][i][j][m]["maxres"]["url"]
                                filtered_data["Data"][i].update({"Thumbnail Url": url})
                            elif m == "title":
                                filtered_data["Data"][i].update({"Video Title": n})
                            elif m == "description":
                                filtered_data["Data"][i].update({"Video Description": n})
                            elif m == "tags":
                                # turning list of tags into a single string
                                tags = ""
                                for p in range(len(n)):
                                    for q in n[p]:
                                        tags += q
                                    if p < len(n) - 1:
                                        tags += ", "
                                filtered_data["Data"][i].update({"Tags": tags})
                                size = len(data[t]["items"][i][j][m])
                                filtered_data["Data"][i].update({"Number of Tags": size})
                            elif m == "categoryId":
                                filtered_data["Data"][i].update({"Video Category ID": n})
                        continue
                    
                    if j == "statistics":
                        for m, n in data[t]["items"][i][j].items():
                            if m == "viewCount":
                                filtered_data["Data"][i].update({"Visualizations": int(n)})
                            elif m == "likeCount":
                                filtered_data["Data"][i].update({"Likes": int(n)})
                            elif m == "dislikeCount":
                                filtered_data["Data"][i].update({"Dislikes": int(n)})
                            elif m == "favoriteCount":
                                filtered_data["Data"][i].update({"Favorites": int(n)})
                            elif m == "commentCount":
                                filtered_data["Data"][i].update({"Comments": int(n)})
                            
                        # append time request
                        filtered_data["Data"][i].update({"Time request": time})
                        
                        # creating a new dictionary for the next video
                        if i < 200:
                            filtered_data["Data"].append({})
                            
                            # labelling next position process
                            filtered_data["Data"][i].update({"Position": i+1})
        
        except IndexError:
            continue
    
    return filtered_data


# This function will filter channels related data
def channel_filter(data, video_data):
    logger.info("Filtering channel data junk...")
    
    # making the data more accessible
    data = data["channels_info"]
    
    for i in itertools.count(0):
        try:
            for j, k in data[i]["items"][0].items():
                if j == "etag":
                    video_data["Data"][i].update({"Channel E-tag": k})  # insuring labeling "Video etag"
                if j == "id":
                    video_data["Data"][i].update({"Channel ID": k})  # insuring labeling "Video etag"
                
                if j == "snippet":
                    for m, n in data[i]["items"][0][j].items():
                        if m == "title":
                            video_data["Data"][i].update({"Channel Title": n})
                            continue
                        if m == "description":
                            video_data["Data"][i].update({"Channel Description": n})
                            continue
                        if m == "publishedAt":
                            video_data["Data"][i].update({"Channel Creation Date": n[:10]})
                            continue
                        
                        if "country" in data[i]["items"][0][j] and m == "country":
                            video_data["Data"][i].update({"Channel Country": n})
                        else:
                            video_data["Data"][i].update({"Channel Country": "Unknown"})
                
                if j == "statistics":
                    for m, n in data[i]["items"][0][j].items():
                        if m == "viewCount":
                            video_data["Data"][i].update({"Channel Views": int(n)})
                        if m == "subscriberCount":
                            video_data["Data"][i].update({"Channel Subscribers": int(n)})
                        if m == "videoCount":
                            video_data["Data"][i].update({"Channel Videos Published": int(n)})
        except IndexError:
            break
    
    return video_data


# This function will construct the data of Time Query and Trend Date
# It is not the best way to call it, but it uses less code (instead of calling main, again)
def time_construct(data):
    
    # we cannot change sized of a dictionary inside a loop
    new_data = {"Data": []}
    
    for i in range(len(data["Data"])):
        new_data["Data"].append({})
        for j, k in data["Data"][i].items():

            if j != "Time request":
                new_data["Data"][i].update({j: k})
            else:

                # making the time request
                time_request = k
                time_pattern = re.compile(r"\d\d:\d\d:\d\d")
                time = str(re.search(time_pattern, time_request))
                time = time[-10:-2]

                # making the date request
                date_request = k
                date_pattern = r"\D\D\D \d\d"
                date = str(re.search(date_pattern, date_request))
                if re.search("Sept", date_request) is not None:
                    date = date[-9: -2] + " 2019"
                else:
                    date = date[-8: -2] + " 2019"

                # updating dictionary
                new_data["Data"][i].update({"Query Time": time})
                new_data["Data"][i].update({"Trending Date": date})
    
    return new_data


# This function will insert the ID Query and the ID Query Name
def id_construct(data, **kwargs):
    new_data = {"Data": []}
    for i in range(len(data["Data"])):
        new_data["Data"].append({})
        
        for j, k in data["Data"][i].items():
            new_data["Data"][i].update({j: k})
        
        # Getting information about Query
        category = kwargs.get("category")
        new_data["Data"][i].update({"Query ID": category})
        id_name = DICTIONARY_BR[category]
        new_data["Data"][i].update({"Query ID Name": id_name})
        
        # Getting name of the Video Category ID.
        try:
            # converting string to integer
            category_id = int(data["Data"][i]["Video Category ID"])
            new_data["Data"][i].update({"Video Category ID": category_id})

            # assign name of category from dictionary
            category_name = DICTIONARY_BR[category_id]
            new_data["Data"][i].update({"Video Category Name": category_name})
        except KeyError:
            new_data["Data"][i].update({"Video Category Name": "ERROR"})
        
    return new_data


# ---------------------------------------------------------------------------------------------------------------------


def categories_filter(data):
    logger.info("Filtering categories data junk...")


def channels_from_categories_filter(data):
    logger.info("Filtering channels from categories data junk...")


# ---------------------------------------------------------------------------------------------------------------------

# This function will include index for the final dictionary to be written
def create_dict(data):
    logger.info("Creating dictionary from the data...")
    
    new_data = {"Data": []}
    
    # Just adding some index for when we need to concatenate multiple data sets
    for i in range(len(data["Data"])):
        new_data["Data"].append({})
        
        for l, k in data["Data"][i].items():
            new_data["Data"][i].update({l: k})

        data["Data"][i].update({"Index": i + 1})
    
    return new_data

# ---------------------------------------------------------------------------------------------------------------------


# And last, this function will just remove some bad characters from strings
def string_correction(data):
    strings_to_correct = ["Video Description",
                          "Video Tittle",
                          "Channel Title",
                          "Channel Description"]
    logger.info("Applying string corrections...")
    bad_chars = re.compile(r"\n|\r")

    for i in range(len(data["Data"])):
        for k, l in data["Data"][i].items():
            if k in strings_to_correct:
                data["Data"][i].update({k: re.sub(bad_chars, "", l)})
                
    return data
