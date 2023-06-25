""" Reference
Test Authentication on XAMPP and mysql-connector module.
Ignore on build.
"""
import mysql.connector
from mysql.connector import Error
from .setup.init_db import *

class DBConnect:

    def __init__(self):
        # Database connection protocol
        self.db = mysql.connector.connect(
            host = sql_dbconfig.g_host,
            port = sql_dbconfig.g_port,
            user = sql_dbconfig.g_user,
            password = sql_dbconfig.g_password,
            database = sql_dbconfig.g_defaultdb
        )




class DBSystem(DBConnect):
    def __init__(self) -> None:
        super().__init__()

    def SearchUserByEmail(self, email:str) -> list | None:
        # Get existing user information if any.
        # returns {grouped_data: dict, None: None}
        grouped_data = self.QueryAccountData()
        for idx in range(len(grouped_data)):
                if grouped_data[idx]["email"] == email:
                    return grouped_data[idx]

    def SearchUserByUsername(self, username:str) -> list | None:
        # Get existing user information if any.
        # returns {grouped_data: dict, None: None}
        grouped_data = self.QueryAccountData()
        for idx in range(len(grouped_data)):
                if grouped_data[idx]["username"] == username:
                    return grouped_data[idx]


    def QueryAccountData(self) -> list:
        
        with self.db.cursor() as cursor:
            # SQL Query
            self.search_sql = "SELECT * FROM tbl_accounts"
            cursor.execute(self.search_sql)
            findings = cursor.fetchall()

            #  Get the column names
            legend = [column[0] for column in cursor.description]

            # Making a list of dictionaries to represent data
            results = []
            for data in findings:
                row_dict = dict(zip(legend, data))
                results.append(row_dict)
            return results
        
    def RegisterUserAccount(self, fname: str, lname: str, username:str, email: str, password: str, role: str) -> None:
            
            with self.db.cursor() as cursor:

                # SQL Query
                self.insert_query = f"INSERT INTO tbl_accounts (first_name, last_name, username, email, password, role) VALUES ('{fname}', '{lname}', '{username}', '{email}', '{password}', '{role}')"

                cursor.execute(self.insert_query)
                self.db.commit()


# Testing purposes
if __name__ == "__main__":
    db_instance = DBSystem()
    print(db_instance.SearchUserByEmail("teacherdo.com")) # passed
    print(db_instance.SearchUserByEmail("johndoe@gmail.com")) # passed
    print(db_instance.SearchUserByEmail("teacherdoe@gmail.com")) # passed
    print(db_instance.SearchUserByUsername("John Doe"))