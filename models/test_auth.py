""" Reference
Test Authentication on XAMPP and mysql-connector module.
Ignore on build.
"""
import mysql.connector
from mysql.connector import Error

class DBConnect:

    def __init__(self):
        # Database connection protocol
        self.db = mysql.connector.connect(
            host="localhost",
            database="db_csystem",
            user="root",
            passwd="test"
        )




class DBSystem(DBConnect):
    def __init__(self):
        super().__init__(self)

    def RegisterUser(self):
        try:
            # SQL Query
            query = "SELECT * FROM tbl_accounts"
            # Database connection using cursor. I don't know how it work, but it works.
            cursor = self.db.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            print(f"Number of records in the table:{cursor.rowcount}\nRecords: {results}")
            
        except Error as error:
            print(f"Failed: {error}")
        finally:
            # Close once connected.
            if self.db.is_connected():
                cursor.close()
                self.db.close()
                print("Connection Closed")
