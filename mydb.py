import mysql.connector

try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='sql@123'
    )

    cursorObject = database.cursor()

    cursorObject.execute("CREATE DATABASE Crm")

    print("Database created successfully!")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if database:
        database.close()
