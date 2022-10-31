import argparse
import sys






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
