from application.config.paths import FILES_OUTPUT_PATH

content = (
    "I'll take your brain to another dimension. "
    "I'm gone sent into outer space - to find another race. "
    "I'm gone sent into outer space - to find another race. "
    "I'm gone sent into outer space - to find another race. "
    "I'll take your brain to another dimension. "
    "I'll take your brain to another dimension. "
    "I'll take your brain to another dimension. "
    "Pay close attention. "
)

file_name: str = "some_txt_file.txt"


def actions_with_file():
    path_to_file = FILES_OUTPUT_PATH.joinpath(file_name)
    with open(path_to_file, mode="w") as txt_file:
        txt_file.write(content)
        txt_file.close()
        return path_to_file
