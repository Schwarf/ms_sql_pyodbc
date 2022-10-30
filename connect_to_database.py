import argparse
import sys

import alembic.config
import alembic.command
import pyodbc


def get_database_connection(password_file: str) -> pyodbc.Connection:
    driver = "ODBC Driver 17 for SQL Server"
    server = 'localhost'
    database = 'Test'
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    connection = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
    return connection

def upgrade_database_scheme(sqlalchemy_url: str) -> None:
    alembic_config = alembic.config.Config("alembic.ini")
    alembic_config.set_main_option("sqlalchemy.url", sqlalchemy_url)
    alembic.command.upgrade(config=alembic_config, revision="head")


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()

    connection = get_database_connection(arguments.password_file)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sys.database_principals ")
    for row in cursor.fetchall():
        print(row)


if __name__ == "__main__":
    main()
