import pyodbc

try:
    connection = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)}; DBQ=C:\Users\Lanz Andrei\OneDrive\Documents\Database2.accdb;')
    print("Database is Connected")

    NewRecord = (10, 'Lanz Andrei A. Catamisan', 18, 'BSCPE', 'Cavite', 90)

    database = connection.cursor()
    database.execute('INSERT INTO Table1 VALUES (?,?,?,?,?,?)', NewRecord)
    connection.commit()

    print("Record is inserted")

except pyodbc.Error:
    print("Database is NOT connected")