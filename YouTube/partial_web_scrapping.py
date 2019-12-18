import urllib.request
import re
import bs4


def web_scrapping_manager(data):
    print("Initializing manual web scrapping process...")
    new_data = {"Data": []}
    
    for i in range(len(data["Data"])):
        new_data["Data"].append({})
        
        for j, k in data["Data"][i].items():
            new_data["Data"][i].update({j: k})
            
            # getting video duration
            if j == "Video ID":
                print(f"........Getting Video {i+1} time duration")
                duration = get_video_duration(k)
                new_data["Data"][i].update({"Video Duration (s)": duration})
    
    return new_data


# This function will return the time duration os each video
def get_video_duration(html):
    
    # getting video html source code
    html = f"https://www.youtube.com/watch?v={html}"
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
        return "ERROR"


def convert_to_seconds(time):
    time = time[21:]
    return int(time)/1000
