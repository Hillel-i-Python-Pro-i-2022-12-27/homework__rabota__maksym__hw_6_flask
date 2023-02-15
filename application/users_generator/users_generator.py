from faker import Faker
from application.config.paths import FILES_OUTPUT_PATH
import json

faker = Faker()

file_name: str = "users_with_emails"


def generation_users_to_json():
    path_to_file = FILES_OUTPUT_PATH.joinpath(file_name)
    data = []
    with open(path_to_file, mode="w") as file:
        for _ in range(10):
            dict_ = {"name": f"{faker.name()}", "email": f"{faker.email()}"}
            data.append(dict_)
        json.dump(data, file, indent=4)
        file.close()
        return path_to_file


def users_from_json_file(path_to_file=generation_users_to_json()):
    with open(path_to_file) as json_file:
        data_json = json.load(json_file)
        return data_json
