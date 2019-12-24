from googleapiclient.discovery import build
from z_sandbox.writer import write


def init_youtube_api():
    print("Initializing YouTube Api V3...")
    
    api_key = init_key()
    api = build("youtube", "v3", developerKey=api_key)
    return api


def init_key():
    print("Gathering user developer Key...")
    
    with open("C:/Users/maruc/OneDrive/Área de Trabalho/WData/a_data_processing/YouTube/config/Key.txt", 'r') as code:
        api_key = code.readline()
    return api_key


# ---------------------------------------------------------------------------------------------------------------------


# REPORT: not worth of implemetation...
def get_full_detailed_video_info(process):
    
    request = process.videos().list(
        part="contentDetails, status",
        id="HuoRLCt72b4"
    )
    data = request.execute()
    return data

    
if __name__ == "__main__":
    process = init_youtube_api()
    data = get_full_detailed_video_info(process)
    write(data, "videos")