import requests

from application.logging.loggers import get_core_logger


def request_astronauts():
    logger = get_core_logger()
    url = "http://api.open-notify.org/astros.json"

    with requests.Session() as session:
        response = session.get(url)
        logger.info(f"{response=}")
        response_json = response.json()
        logger.info(f"{response_json}")

        return response_json
