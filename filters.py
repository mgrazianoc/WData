import re
import itertools
import YouTube.web_scrapping
import YouTube.config.constants as constants


def filter_manager(data, parse):
    if parse.task == "trends":
        # This function will filter videos related data
        filtered_data = videos_filter(data)
        
        # This function will filter channels related data
        filtered_data = channel_filter(data, filtered_data)
        
        # This function will include each videos durations in seconds (integer)
        extra_data = YouTube.web_scrapping.web_scrapping_manager(filtered_data)
        
        # This function will construct the data of Time Query and Trend Date
        extra_data = time_construct(extra_data)
        
        # This function will insert the ID Query and the ID Query Name
        extra_data = id_construct(extra_data, parse)
        
        # This function will include index for the final dictionary to be written
        final_data = create_dict(extra_data)
        
        # And last, this function will just remove some bad characters from strings
        final_data = string_correction(final_data)
        
        return final_data


# ---------------------------------------------------------------------------------------------------------------------


def videos_filter(data):
    print("Filtering videos data junk...")
    
    # constructing dictionary structure
    filtered_data = {"Data": []}
    filtered_data["Data"].append({})
    
    # labelling first position process
    position = len(filtered_data["Data"])
    filtered_data["Data"][position - 1].update({"Position": position})
    
    # making the data more accessible
    data = data["most_popular"]
    
    # there are 4 lists of items to separate. Each items has a list of dictionaries
    
    time = data[4]
    
    for t in range(4):
        try:
            for i in itertools.count(0):
                for j, k in data[t]["items"][i].items():
                    # filtering process
                    if j == "etag":
                        filtered_data["Data"][position - 1].update({"Video E-tag": k})  # insuring labeling "Video etag"
                        continue
                        
                    if j == "id":
                        filtered_data["Data"][position - 1].update({"Video ID": k})  # insuring labeling "Video Id"
                        continue
                    
                    if j == "snippet":
                        for m, n in data[t]["items"][i][j].items():
                            if m == "PublishedAt":
                                filtered_data["Data"][position - 1].update({"Publication Date": n[:10]})
                                filtered_data["Data"][position - 1].update({"Publication Time": n[11:19]})
                            if m == "thumbnails":
                                url = data[t]["items"][i][j][m]["maxres"]["url"]
                                filtered_data["Data"][position - 1].update({"Thumbnail Url": url})
                            elif m == "title":
                                filtered_data["Data"][position - 1].update({"Video Title": n})
                            elif m == "description":
                                filtered_data["Data"][position - 1].update({"Video Description": n})
                            elif m == "tags":
                                tags = ""
                                for p in range(len(m)):
                                    tags += m[p] + ", "
                                filtered_data["Data"][position-1].update({"Tags": tags})
                                filtered_data["Data"][position - 1].update({"Number of Tags": len(m)})
                        continue
                    
                    if j == "statistics":
                        for m, n in data[t]["items"][i][j].items():
                            if m == "viewCount":
                                filtered_data["Data"][position - 1].update({"Visualizations": n})
                            elif m == "likeCount":
                                filtered_data["Data"][position - 1].update({"Likes": n})
                            elif m == "dislikeCount":
                                filtered_data["Data"][position - 1].update({"Dislikes": n})
                            elif m == "favoriteCount":
                                filtered_data["Data"][position - 1].update({"Favorites": n})
                            elif m == "commentCount":
                                filtered_data["Data"][position - 1].update({"Comments": n})
                            
                        # append time request
                        filtered_data["Data"][position - 1].update({"Time request": time})
                        
                        # creating a new dictionary for the next video
                        if position < 200:
                            filtered_data["Data"].append({})
                            
                            # labelling next position process
                            position = len(filtered_data["Data"])
                            filtered_data["Data"][position - 1].update({"Position": position})
        
        except IndexError:
            continue
    
    return filtered_data


def channel_filter(data, video_data):
    print("Filtering channel data junk...")
    
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
                        if m == "description":
                            video_data["Data"][i].update({"Channel Description": n})
                        if m == "publishedAt":
                            video_data["Data"][i].update({"Channel Date": n})
                
                if j == "statistics":
                    for m, n in data[i]["items"][9][j].items():
                        if m == "viewCount":
                            video_data["Data"][i].update({"Channel Views": n})
                        if m == "subscriberCount":
                            video_data["Data"][i].update({"Channel Subscribers": n})
                        if m == "videoCount":
                            video_data["Data"][i].update({"Channel videos count": n})
        except IndexError:
            break
    
    return video_data


def time_construct(data):
    for i in range(len(data["Data"])):
        for j, k in data["Data"][i].items():
            if j != "Time request":
                continue
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
                data["Data"][i].update({"Time Query": time})
                data["Data"][i].update({"Trending Date": date})
    
    return data


def id_construct(data, parse):
    for i in range(len(data["Data"])):
        data["Data"][i].update({"Query ID": parse.category})
        data["Data"][i].update({"Query ID Name": YouTube.config.constants.DICTIONARY_BR[parse.category]})
    
    return data


# ---------------------------------------------------------------------------------------------------------------------


def categories_filter(data):
    print("Filtering categories data junk...")


def channels_from_categories_filter(data):
    print("Filtering channels from categories data junk...")


# ---------------------------------------------------------------------------------------------------------------------


def create_dict(data):
    print("Creating dictionary from the data...")
    
    # Just making some index =)
    for i in range(len(data["Data"])):
        data["Data"][i].update({"Index": i+1})
    
    return data

# ---------------------------------------------------------------------------------------------------------------------


def string_correction(data):
    strings_to_correct = ["Video Description",
                          "Video Tittle",
                          "Channel Title",
                          "Channel Description"]
    print("Applying string corrections to snippet...")
    bad_chars = re.compile(r"\n|\r")

    for i in range(len(data["Data"])):
        for k, l in data["Data"][i]:
            if k in strings_to_correct:
                data["Data"][i].update({k: re.sub(bad_chars, "", l)})
                
    return data
