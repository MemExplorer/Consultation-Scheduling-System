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
            query = "SELECT * FROM tbl_accounts"
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        


# Testing purposes

if __name__ == "__main__":
    db_instance = DBSystem()
    print(db_instance.QueryAccountData()) # passed
    print(db_instance.SearchUser("teacherdoe@gmail.com")) # passed
    print(db_instance.SearchUser("teacherdoe@gmaisl.com")) # passed