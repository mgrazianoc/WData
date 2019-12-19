import json


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


def write_file(data, parser):
    print("Writing data in file...")
    data = json_format(data)
    with open(
            f"a_data_process/output/Yahoo/{parser.task}_{parser.country}.json",
            "w",
            encoding="utf-8") as file:
        file.write(str(data))
