import argparse
import os
import sys

import alembic.command
import alembic.config
import pyodbc


def get_pyodbc_connection_string(password_file: str) -> str:
    driver = "ODBC Driver 17 for SQL Server"
    server = 'localhost'
    database = 'Test'
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    url = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    return url


def get_sql_alchemy_url(password_file: str) -> str:
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    server = 'localhost'
    database = 'Test'
    driver = "ODBC+Driver+17+for+SQL+Server"
    url = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
    return url


def set_sql_alchemy_env_variable(password_file: str) -> None:
    url = get_sql_alchemy_url(password_file)
    sqlalchemy_env_variable = "SQLALCHEMY_URL"
    os.environ[sqlalchemy_env_variable] = url


def get_database_connection(password_file: str) -> pyodbc.Connection:
    url = get_pyodbc_connection_string(password_file)
    connection = pyodbc.connect(url)
    return connection


def upgrade_database_scheme(password_file: str) -> None:
    alembic_config = alembic.config.Config("alembic.ini")
    set_sql_alchemy_env_variable(password_file)
    alembic.command.upgrade(config=alembic_config, revision="head")


def main() -> None:
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("--password_file", required=True)
    try:
        arguments = argument_parser.parse_args()
    except ValueError as error:
        print("Arguments are not valid")
        sys.exit()

    # connection = get_database_connection(arguments.password_file)
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM sys.database_principals ")
    # for row in cursor.fetchall():
    #    print(row)
    upgrade_database_scheme(arguments.password_file)


if __name__ == "__main__":
    main()
