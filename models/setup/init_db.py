""" Pre-defined Database Design

This is a pre-defined design for the database structure so you can write sql code in the "./csystem.sql" file.
"""

import mysql.connector
from . import sql_dbconfig

def initialize_database() -> bool:
    try:
        # Connect to the database
        db = mysql.connector.connect(
            host = sql_dbconfig.g_host,
            port = sql_dbconfig.g_port,
            user = sql_dbconfig.g_user,
            password = sql_dbconfig.g_password
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

        return True
    except mysql.connector.Error as error:
        print(f"Error during database initialization: {error}")
        return False
