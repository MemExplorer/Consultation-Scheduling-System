import mysql.connector

try:
    # Try to connect to the existing db_csystem database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test",
        database="db_csystem"
    )
    db_connected = True
except mysql.connector.Error as error:
    db_connected = False

if db_connected:
    # The db_csystem database already exists, proceed with the code as before
    cursor = db.cursor()

    # Read the contents of data.sql
    with open('/models/csystem.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL commands from data.sql
    cursor.execute(sql_script)

    # Commit the changes to the database
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    db.close()
else:
    # Create a new db_csystem database and populate it with table and values from csystem.sql
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="test"
    )
    cursor = db.cursor()

    # Create the db_csystem database
    cursor.execute("CREATE DATABASE db_csystem")

    # Use the db_csystem database
    cursor.execute("USE db_csystem")

    # Read the contents of data.sql
    with open('/models/csystem.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL commands from data.sql
    cursor.execute(sql_script)

    # Commit the changes to the database
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    db.close()