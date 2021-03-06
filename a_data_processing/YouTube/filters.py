import re
from a_data_processing.YouTube.partial_web_scrapping import web_scrapping_manager
from a_data_processing.YouTube.config.constants import DICTIONARY_BR
from wdata_config.loggers import create_info_log

from a_data_processing.YouTube.writer import temp_write

logger = create_info_log(__name__)


# ---------------------------------------------------------------------------------------------------------------------

def filter_manager(data, **kwargs):
    logger.info("Initiating filter_manager")
    if kwargs.get("task") == "trends":
        
        temp_write(data, "testando1", **kwargs)
        
        filtered_data = videos_filter(data)
        temp_write(filtered_data, "testando2", **kwargs)
        
        filtered_data = channel_filter(data, filtered_data)
        temp_write(filtered_data, "testando3", **kwargs)
        
        extra_data = web_scrapping_manager(filtered_data)
        temp_write(extra_data, "testando4", **kwargs)
        
        extra_data = time_construct(extra_data)
        temp_write(extra_data, "testando5", **kwargs)
        
        extra_data = id_construct(extra_data, **kwargs)
        temp_write(extra_data, "testando6", **kwargs)
        
        final_data = create_index(extra_data)
        temp_write(final_data, "testando7", **kwargs)
        
        final_data = string_correction(final_data)
        temp_write(final_data, "testando8", **kwargs)
        
        final_data = create_order(final_data)
        temp_write(final_data, "testando9", **kwargs)
        
        return final_data

# ---------------------------------------------------------------------------------------------------------------------


# This function will filter videos related data
def videos_filter(data):
    logger.info("Filtering videos data junk...")
    
    # constructing dictionary structure
    filtered_data = {"Data": []}
    
    # making the data more accessible
    data = data["most_popular"]
    
    # time of query request position
    time = data.pop(-1)
    
    for t in range(len(data)):

        for i in range(len(data[t]["items"])):
            
            # since i range doesn't go higher then len(data[t]["items"]), track is used to count t repetitions as well
            track = t*50 + i
            
            
            filtered_data["Data"].append({})
            filtered_data["Data"][track].update({"Position": track+1})
            
            for j, k in data[t]["items"][i].items():
                # filtering process
                if j == "etag":
                    filtered_data["Data"][track].update({"Video_Etag": k})  # insuring labeling "Video etag"

                elif j == "id":
                    filtered_data["Data"][track].update({"Video_ID": k})  # insuring labeling "Video Id"

                elif j == "snippet":
                    for m, n in k.items():
                        if m == "publishedAt":
                            filtered_data["Data"][track].update({"Publication_Date": n[:10]})
                            filtered_data["Data"][track].update({"Publication_Time": n[11:19]})
                        if m == "thumbnails":
                            url = n["maxres"]["url"]
                            filtered_data["Data"][track].update({"Thumbnail_Url": url})
                        elif m == "title":
                            filtered_data["Data"][track].update({"Video_Title": n})
                        elif m == "description":
                            filtered_data["Data"][track].update({"Video_Description": n})
                        elif m == "tags":
                            # turning list of tags into a single string
                            tags = ""
                            for p in range(len(n)):
                                for q in n[p]:
                                    tags += q
                                if p < len(n) - 1: # just avoiding a ", " at the final of the string
                                    tags += ", "
                            filtered_data["Data"][track].update({"Tags": tags})
                            filtered_data["Data"][track].update({"Number_of_Tags": len(n)})
                        elif m == "categoryId":
                            filtered_data["Data"][track].update({"Video_Category_ID": n})

                elif j == "statistics":
                    for m, n in k.items():
                        if m == "viewCount":
                            filtered_data["Data"][track].update({"Visualizations": int(n)})
                        elif m == "likeCount":
                            filtered_data["Data"][track].update({"Likes": int(n)})
                        elif m == "dislikeCount":
                            filtered_data["Data"][track].update({"Dislikes": int(n)})
                        elif m == "favoriteCount":
                            filtered_data["Data"][track].update({"Favorites": int(n)})
                        elif m == "commentCount":
                            filtered_data["Data"][track].update({"Comments": int(n)})

                    # append time request
                    filtered_data["Data"][track].update({"Time request": time})
    
    return filtered_data


# This function will filter channels related data
def channel_filter(data, video_data):
    logger.info("Filtering channel data junk...")
    
    # making the data more accessible
    data = data["channels_info"]
    
    
    for i in range(len(data)):
        for j, k in data[i]["items"][0].items():
            if j == "etag":
                video_data["Data"][i].update({"Channel_Etag": k})  # insuring labeling "Video etag"
            elif j == "id":
                video_data["Data"][i].update({"Channel_ID": k})  # insuring labeling "Video etag"

            elif j == "snippet":
                for m, n in k.items():
                    if m == "title":
                        video_data["Data"][i].update({"Channel_Title": n})
                    elif m == "description":
                        video_data["Data"][i].update({"Channel_Description": n})
                    elif m == "publishedAt":
                        video_data["Data"][i].update({"Channel_Creation_Date": n[:10]})

                    # sometimes, API doesn't return the channels country
                    if "country" not in k:
                        video_data["Data"][i].update({"Channel_Country": "Unknown"})
                    elif m == "country":
                        video_data["Data"][i].update({"Channel_Country": n})

            if j == "statistics":
                for m, n in k.items():
                    if m == "viewCount":
                        video_data["Data"][i].update({"Channel_Views": int(n)})
                    elif m == "subscriberCount":
                        video_data["Data"][i].update({"Channel_Subscribers": int(n)})
                    elif m == "videoCount":
                        video_data["Data"][i].update({"Channel_Videos_Published": int(n)})
    
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
                new_data["Data"][i].update({"Query_Time": time})
                new_data["Data"][i].update({"Query_Date": date})
    
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
        new_data["Data"][i].update({"Query_ID": category})
        id_name = DICTIONARY_BR[category]
        new_data["Data"][i].update({"Query_ID_Name": id_name})
        
        # Getting name of the Video Category ID.
        try:
            # converting string to integer
            category_id = int(data["Data"][i]["Video_Category_ID"])
            new_data["Data"][i].update({"Video_Category_ID": category_id})

            # assign name of category from dictionary
            category_name = DICTIONARY_BR[category_id]
            new_data["Data"][i].update({"Video_Category_Name": category_name})
        except KeyError:
            new_data["Data"][i].update({"Video_Category_Name": "ERROR"})
        
    return new_data


# ---------------------------------------------------------------------------------------------------------------------


def categories_filter(data):
    logger.info("Filtering categories data junk...")


def channels_from_categories_filter(data):
    logger.info("Filtering channels from categories data junk...")


# ---------------------------------------------------------------------------------------------------------------------

# This function will include index for the final dictionary to be written
def create_index(data):
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


# This function will just remove some bad characters from strings
def string_correction(data):
    strings_to_correct = ["Video_Description",
                          "Video_Tittle",
                          "Channel_Title",
                          "Channel_Description"]
    logger.info("Applying string corrections...")
    bad_chars = re.compile(r"\n|\r")

    for i in range(len(data["Data"])):
        for k, l in data["Data"][i].items():
            if k in strings_to_correct:
                data["Data"][i].update({k: re.sub(bad_chars, "", l)})
                
    return data


# ---------------------------------------------------------------------------------------------------------------------

# This function will just create a somewhat ordered dictionary
# The reason for that is that it makes easier to export do .db, since we have a standard model in all aplication
def create_order(data):
    logger.info("Ordering the data...")
    
    new_data = {"Data": []}
    order = ["Query_ID", "Query_ID_Name", "Query_Date", "Query_Time",
             "Position", "Video_ID", "Video_Title", "Video_Description", "Video_Category_ID", "Video_Category_Name",
             "Tags", "Number_of_Tags", "Publication_Date", "Publication_Time", "Video_duration_s", "Thumbnail_Url",
             "Visualizations", "Likes", "Dislikes", "Favorites", "Comments", "Channel_ID", "Channel_Title",
             "Channel_Country", "Channel_Description", "Channel_Creation_Date", "Channel_Views", "Channel_Subscribers",
             "Channel_Videos_Published", "Video_Etag", "Channel_Etag"]
    
    for i in data["Data"]:
        new_data["Data"].update({})
        for j in order:
            for k, l in i.items():
                if k == j:
                    new_data.update({k:l})
    
    return new_data
    
    