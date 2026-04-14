import json
import os

from utils.logger import timestamp


def write_json(data , folder_name, file_type):

    base_dir = os.path.join("api_logs", folder_name)
    os.makedirs(base_dir, exist_ok=True)

    file_path =os.path.join(base_dir,f"{file_type}_{timestamp}.json")

    with open(file_path , "w") as file:
        json.dump(data , file, indent=4)

    return  file_path
