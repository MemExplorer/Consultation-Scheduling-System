""" Pre-defined Database Design

This is a pre-defined design for the database structure so you can write sql code in the "./csystem.sql" file.
"""

import mysql.connector

try:
    # Connect to the database
    db = mysql.connector.connect(
        host="localhost",
        user="root", # Change this based on your MySQL configuration
        password="test" # Change this based on your MySQL configuration
    )

    # Create a cursor object
    cursor = db.cursor()

    # Read the contents of csystem.sql
    with open('./models/csystem.sql', 'r') as file:
        sql_script = file.read()

    # Execute the SQL commands from csystem.sql
    for result in cursor.execute(sql_script, multi=True):
        pass

    # Commit the changes to the database
    db.commit()

    # Close the cursor and database connection
    cursor.close()
    db.close()

    print("Database initialization completed successfully.")

except mysql.connector.Error as error:
    print(f"Error during database initialization: {error}")
