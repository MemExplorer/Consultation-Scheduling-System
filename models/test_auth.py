""" Reference
Test Authentication on XAMPP and mysql-connector module.
Ignore on build.
"""
import mysql.connector
from mysql.connector import Error

# Database connection protocol
db = mysql.connector.connect(
    host="localhost",
    database="db_csystem",
    user="root",
    passwd="test"
)

# Handle error on queries
try:

    # SQL Query
    query = "SELECT * FROM tbl_accounts"

    # Database connection using cursor. I don't know how it work, but it works.
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    print(f"Number of records in the table:{cursor.rowcount}\nRecords: {results}")

except Error as error:
    print(f"Failed: {error}")

finally:
    # Close once connected.
    if db.is_connected():
        cursor.close()
        db.close()
        print("Connection Closed")