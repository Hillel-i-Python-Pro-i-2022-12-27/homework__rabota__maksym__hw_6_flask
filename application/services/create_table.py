from application.services.db_connection import DBConnection


def create_table():
    with DBConnection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS phones (
                pk INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                contact_name VARCHAR NOT NULL,
                phone_value INTEGER NOT NULL
            )
        """
        )
