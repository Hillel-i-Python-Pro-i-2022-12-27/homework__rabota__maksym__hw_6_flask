import requests

from application.average.avarage_params import average_params
from application.config.paths import FILES_OUTPUT_PATH
from application.logging.loggers import get_core_logger


def get_csv():
    logger = get_core_logger()
    url = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"

    path_to_file = FILES_OUTPUT_PATH.joinpath("hw.csv")

    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response=}")

        csv_file = open(path_to_file, "wb")
        csv_file.write(response.content)
        csv_file.close()

    logger.info(f"\nPath to file: file://{path_to_file}\nDONE.\n\n" f"Average is.\n{average_params()}")
