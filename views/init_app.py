""" Application Interface Module

This file is modified to run using a runner file defined in the run.py file.
If you wish to test this file change all import paths to its relative path.

Because this file imports are based on the run.py relative paths, you cannot run this file as a "__main__".


File definition:
init_app is the application interface for login/signup window before the user authenticate/register into the database.
"""


import customtkinter as ctk
from views._main import MainFrame
from views._login import LogInFrame # Based on the run.py path, you cannot run this file alone.


# Initial frame class for each window
class App(ctk.CTk):
    width = 900
    height = 600

    def __init__(self):
        super().__init__()

        #Configure Window
        self.geometry(f"{self.width}x{self.height}")
        self.title("CvSU-Carmona Campus Consultation Scheduling System")

        self.configure(fg_color="black")

        """""
        image_path = os.path.join(os.path.dirname(os.path.realpath("./resources/images/")), "images")
        
        self.Bg_Img = ctk.CTkImage(Image.open(os.path.join(image_path, "pyimage1.png")), size=(self.width, self.height))
        self.Bg_Label = ctk.CTkLabel(self, text="", image = self.Bg_Img)
        self.Bg_Label.pack()
        """""

        #Configure Main Frame
        self.MainFrame = MainFrame(master=self)
        self.MainFrame.place(relx=0.5, rely=0.5, anchor="center")
        self.MainFrame.configure(fg_color="white")

        #Configure Log In Frame. Login frame generated from the _login.py, _file.py means that it is a ctk frame.
        self.LogIn_frame = LogInFrame(master=self)
        self.LogIn_frame.configure(fg_color="white")

app = App()

# On instance run as main file. To test the program file only, not accessible as a module reference.
if __name__ == "__main__":
    app.mainloop()