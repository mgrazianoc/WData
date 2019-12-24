import json


def json_format(data):
    print("Converting data into .JSON format...")
    json_data = json.dumps(data, indent=2)
    return json_data


def write(data, file_name):
    data = json_format(data)
    
    print("Writing data in file...")
    with open(f"C:/Users/maruc/OneDrive/Área de Trabalho/WData/z_sandbox/{file_name}.json", "w") as testing:
        testing.write(str(data))

