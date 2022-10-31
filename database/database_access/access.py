import pyodbc


def get_pyodbc_connection_string(password_file: str) -> str:
    driver = "ODBC Driver 17 for SQL Server"
    server = 'localhost'
    database = 'crawler_db'
    with open(password_file, "r") as file:
        lines = file.read().splitlines()
        username = lines[0]
        password = lines[1]
        file.close()
    url = f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    return url


def get_database_connection(password_file: str) -> pyodbc.Connection:
    url = get_pyodbc_connection_string(password_file)
    connection = pyodbc.connect(url)
    return connection
