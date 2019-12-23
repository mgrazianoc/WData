from wdata_config.loggers import create_info_log as create_info_log

import time
import json


logger = create_info_log(__name__)

# ---------------------------------------------------------------------------------------------------------------------


def write_file(data, **kwargs):
    data = json_format(data)
    logger.info("Writing data in file...")

    # for direct/routine call
    
    if kwargs.get("name") != "standard":
        file_name = kwargs.get("name")
    else:
        category = kwargs.get("category")
        country = kwargs.get("country")
        task = kwargs.get("task")
        file_name = f"categ{category}_{time.strftime('%y.%m.%d')}_{country}_{task}.json"
    
    with open(f"{kwargs.get('output')}/{file_name}", "w", encoding="utf-8") as file:
        file.write(str(data))


def json_format(data):
    logger.info("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data

# ---------------------------------------------------------------------------------------------------------------------


# This functions is just for debugging purpose, only direct call
def temp_write(data, output):
    data = json_format(data)
    print("Writing data in file...")
    with open(f"{output}Testing.json", "w") as testing:
        testing.write(str(data))
