""" 
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from views import main_init

class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Python Routing Methods
        def ToLogin():
            self.destroy()
            main_init.app.configure(fg_color="pink")
            main_init.app.LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

        def ToSignUp():
            main_init.app.destroy() # Change this on _signup.py

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Login", command=ToLogin)
        self.LogIn_btn.grid(row=14, column=0, padx=10, pady=15)

        #Sign Up Button
        self.SignUp_btn = ctk.CTkButton(self, text="Sign up", command=ToSignUp)
        self.SignUp_btn.grid(row=14, column=1, padx=10, pady=15)