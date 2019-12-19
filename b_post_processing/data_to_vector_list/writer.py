import json


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


def write_file(data):

    data = json_format(data)
    print("Writing data in file...")

    with open(
            f"C:/Users/maruc/OneDrive/Área de Trabalho/Data Science/b_post_processing/data_frame_organize/output/testing.json",
            "w") as file:
        file.write(str(data))
