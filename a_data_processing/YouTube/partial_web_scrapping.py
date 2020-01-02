from wdata_config.decorators import func_time_logger as func_time_logger
from wdata_config.loggers import create_info_log as create_info_log

import urllib.request
import re
import bs4


logger = create_info_log(__name__)

@func_time_logger
def web_scrapping_manager(data):
    logger.info("Initializing manual web scrapping process...")
    new_data = {"Data": []}
    
    for i in range(len(data["Data"])):
        new_data["Data"].append({})
        
        for j, k in data["Data"][i].items():
            new_data["Data"][i].update({j: k})
            
            # getting video duration
            if j == "Video_ID":
                logger.info(f"........Getting Video {i+1} time duration")
                duration = get_video_duration(k)
                new_data["Data"][i].update({"Video_Duration_s": duration})
    
    return new_data


# This function will return the time duration os each video
def get_video_duration(video_id):
    
    # getting video html source code
    html = f"https://www.youtube.com/watch?v={video_id}"
    source_code = urllib.request.urlopen(html)
    
    # arranging html code and returning specific id where video duration info can be found
    html = bs4.BeautifulSoup(source_code, features="html.parser")
    html_video_info = html.find(id="player")
    
    # cleaning up junk and returning video duration integer (seconds)
    pattern = re.compile(r"approxDurationMs..:..\d+")
    duration = re.search(pattern, str(html_video_info))
    try:
        duration = convert_to_seconds(duration.group())
        return duration
    except AttributeError:
        logger.info("get_video_duration returned an AttributeError")
        return "ERROR"

def convert_to_seconds(time):
    time = time[21:]
    return int(time)/1000
