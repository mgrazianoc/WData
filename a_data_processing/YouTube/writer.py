import os
import time
import json


def write_file(data, parser):

    # step 2
    data = json_format(data)

    # step 3
    print("Writing data in file...")
    file_name = f"cat{parser.category}_{time.strftime('%y.%m.%d')}_{parser.country}_{parser.task}.json"

    with open(f"a_data_processing/output/YouTube/{file_name}",
              "w", encoding="utf-8") as file:
        file.write(str(data))

    # size_calculator(file_name, parser)


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


