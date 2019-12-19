import json


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


def write_file(data):

    data = json_format(data)
    print("Writing data in file...")

    with open(
            f"a_data_processing/output/Twitter/testing.json",
            "w",
            encoding="utf-8") as file:
        file.write(str(data))
