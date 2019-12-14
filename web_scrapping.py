import urllib.request
import re
import bs4


def web_scrapping_manager(data):
    for i in range(len(data["Data"])):
        for j, k in data["Data"][i]:
            if j != "thumbnail url":
                continue
            else:
                duration = get_video_duration(k)
            
            data["Data"][i].update({"Video Duration (s)": duration})
    return data


def get_video_duration(html):
    html = f"https://www.youtube.com/watch?v={html}"
    source_code = urllib.request.urlopen(html)

    html = bs4.BeautifulSoup(source_code, features="html.parser")
    html_video_info = html.find(id="player")

    pattern = re.compile(r"approxDurationMs..:..\d+")
    duration = re.search(pattern, str(html_video_info))
    duration = convert_to_seconds(duration.group())
    print(duration)
    return duration


def convert_to_seconds(time):
    time = time[21:]
    return int(time)/1000



