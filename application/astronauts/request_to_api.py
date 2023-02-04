import requests

url = "http://api.open-notify.org/astros.json"


def request_astronauts():
    with requests.Session() as session:
        response = session.get(url)
        response_json = response.json()

        return response_json
