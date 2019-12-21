import time
import json


def write_file(data, parser):
    data = json_format(data)
    print("Writing data in file...")

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
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data

# ---------------------------------------------------------------------------------------------------------------------


# This functions is just for debugging purpose, only direct call
def temp_write(data, output):
    data = json_format(data)
    print("Writing data in file...")
    with open(f"{output}Testing.json", "w") as testing:
        testing.write(str(data))
