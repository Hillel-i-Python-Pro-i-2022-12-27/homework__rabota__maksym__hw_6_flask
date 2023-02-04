from application.astronauts.request_to_api import request_astronauts
from application.config.paths import FILES_OUTPUT_PATH

file_name = "astronauts.txt"


def astronauts():
    content = request_astronauts()
    path_to_file = FILES_OUTPUT_PATH.joinpath(file_name)

    with open(path_to_file, mode="w") as file:
        file.write(f"<p>Total astronauts is: {content['number']}<p>")
        for full_name in content["people"]:
            file.write(f"<li>{full_name['name']}<li>\n")

        return path_to_file
