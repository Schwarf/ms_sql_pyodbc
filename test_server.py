import pyodbc


server = 'localhost'
database = 'Test'
username = 'sa'
password = ''
print(server)
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("SELECT * FROM sys.database_principals " )
for row in cursor.fetchall():
    print(row)

