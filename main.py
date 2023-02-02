from application.astronauts.amount_of_astronauts import astronauts
from application.average.get_csv import get_csv
from application.logging.init_logging import init_logging
from application.users_generator.users_file import users_file


def main() -> None:
    # Astronauts names and amount
    astronauts()

    # Generate users
    users_file()

    # Get *.csv file from Google Drive and processing data
    get_csv()


if __name__ == "__main__":
    init_logging()
    main()
