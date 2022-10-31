import os

import alembic.command
import alembic.config


# TODO This function only updates the head, but does not autogenerate the revision
def upgrade_database_scheme(password_file: str) -> None:
    alembic_config = alembic.config.Config("alembic.ini")
    set_sql_alchemy_env_variable(password_file)
    alembic.command.upgrade(config=alembic_config, revision="head")


def set_sql_alchemy_env_variable(password_file: str) -> None:
    url = get_sql_alchemy_url(password_file)
    sqlalchemy_env_variable = "SQLALCHEMY_URL"
    os.environ[sqlalchemy_env_variable] = url
    print(os.environ.get(sqlalchemy_env_variable))


def get_sql_alchemy_url(password_file: str) -> str:
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    server = 'localhost'
    database = 'crawler_db'
    driver = "ODBC+Driver+17+for+SQL+Server"
    url = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver={driver}"
    return url
