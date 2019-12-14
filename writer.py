import os
import time
import json


def write_file(data, parser):

    # step 2
    data = json_format(data)

    # step 3
    print("Writing data in file...")
    file_name = f"cat{parser.category}_{time.strftime('%y.%m.%d')}_{parser.country}_{parser.data}.json"

    with open(f"{parser.output_dir}/{file_name}",
              "w", encoding="utf-8") as file:
        file.write(str(data))

    size_calculator(file_name, parser)


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


def size_calculator(file_name, parser):
    directory = os.getcwd()
    size = os.path.getsize(f"{directory}/{parser.output_dir}/{file_name}")
    print(f"Total of data downloaded: {size} bytes")


# ---------------------------------------------------------------------------------------------------------------------

# This functions is just for debugging purpose
def temp_write(data, output):
    data = json_format(data)
    print("Writing data in file...")
    with open(f"{output}Testing.json", "w") as teste:
        teste.write(str(data))
