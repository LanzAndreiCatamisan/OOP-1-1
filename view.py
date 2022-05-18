import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Lanz Andrei\OneDrive\Documents\Database2.accdb;')
    print("Database is Connected")

    database = connection.cursor()
    database.execute('select * from Table1')
    for x in database.fetchall():
        print(x)

except pyodbc.Error:
    print("Database is NOT connected")