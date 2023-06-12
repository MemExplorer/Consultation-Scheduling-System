""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from views import init_app

class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Python Routing Methods
        def ToLogin():
            self.destroy()
            init_app.app.configure(fg_color="pink")
            init_app.app.LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

        def ToSignUp():
            init_app.app.destroy() # Change this on _signup.py

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Login", command=ToLogin)
        self.LogIn_btn.grid(row=14, column=0, padx=10, pady=15)

        #Sign Up Button
        self.SignUp_btn = ctk.CTkButton(self, text="Sign up", command=ToSignUp)
        self.SignUp_btn.grid(row=14, column=1, padx=10, pady=15)