from views import init_app
from models import init_db

if __name__ == "__main__":
    init_db # Initialize a pre-defined database in the models/csystem.sql
    init_app.init.mainloop() # Runner file for the main_init app. Do not modify unless required.