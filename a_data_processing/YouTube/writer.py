import time
import json


def configuring_logging():
    
    # setting up logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatting = logging.Formatter(
        "%(name)s:%(asctime)s:%(levelname)s:%(message)s")
    
    # creating specific file handler on g_logs
    file_handler = logging.fileHandler("/g_logs/youtube_api.log")
    file_handler.setFormatter(formatting)
    logger.addHandler(file_handler)
    
    # creating stream handler, simple format
    cmd_handler = logging.StreamHandler()
    logger.addHandler(cmd_handler)


# ---------------------------------------------------------------------------------------------------------------------


def write_file(data, parser):
    data = json_format(data)
    logger("Writing data in file...")

    # for direct call
    try:
        file_name = f"cat{parser.category}_{time.strftime('%y.%m.%d')}_{parser.country}_{parser.task}.json"

        with open(f"{parser.output_dir}/{file_name}",
                  "w", encoding="utf-8") as file:
            file.write(str(data))
    # for WData call
    except AttributeError:
        file_name = f"cat{parser['category']}_{time.strftime('%y.%m.%d')}_{parser['country']}_{parser['task']}.json"
        with open(f"{parser['output']}/{file_name}",
                  "w", encoding="utf-8") as file:
            file.write(str(data))


def json_format(data):
    logger("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data

# ---------------------------------------------------------------------------------------------------------------------


# This functions is just for debugging purpose, only direct call
def temp_write(data, output):
    data = json_format(data)
    print("Writing data in file...")
    with open(f"{output}Testing.json", "w") as testing:
        testing.write(str(data))
