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
            user="root", # Change this based on your MySQL configuration
            passwd="test" # Change this based on your MySQL configuration
        )




class DBSystem(DBConnect):
    def __init__(self) -> None:
        super().__init__()

    def SearchUser(self, email:str) -> list:
    
            # Get existing user information if any, returns False on error attempt.
            try:
                 return [list(data) for data in self.QueryAccountData() if any(email in data for data in self.QueryAccountData())][0]
            except:
                 return False

        

    def QueryAccountData(self) -> list:
        
        with self.db.cursor() as cursor:
            # SQL Query
            self.search_sql = "SELECT * FROM tbl_accounts"
            cursor.execute(self.search_sql)
            results = cursor.fetchall()
            return results
        
    def RegisterUserAccount(self, fname: str, lname: str, username:str, email: str, password: str, role: str) -> None:
            
            with self.db.cursor() as cursor:

                # SQL Query
                self.insert_query = f"INSERT INTO tbl_accounts (first_name, last_name, username, email, password, category) VALUES ('{fname}', '{lname}', '{username}', '{email}', '{password}', '{role}')"

                cursor.execute(self.insert_query)
                self.db.commit()


# Testing purposes

if __name__ == "__main__":
    db_instance = DBSystem()
    print(db_instance.QueryAccountData()) # passed
    print(db_instance.SearchUser("teacherdoe@gmail.com")) # passed
    print(db_instance.SearchUser("teacherdoe@gmaisl.com")) # passed