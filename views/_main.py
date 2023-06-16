""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from views import init_app

class TitleFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Consultation System", font=("Roboto", 80, "bold"), text_color="Black")
        self.titleLabel.grid(rowspan=5, columnspan=3, padx=10, pady=10, sticky="nsew")

class OptionFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Python Routing Methods
        def ToLogin():
            self.destroy()
            init_app.init.TitleFrame.destroy()
            init_app.init.LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

        def ToSignUp():
            self.destroy()
            init_app.init.TitleFrame.destroy()
            init_app.init.SignUp_frame.place(relx=0.5, rely=0.5, anchor="center")

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Login", command=ToLogin)
        self.LogIn_btn.grid(row=0, column=0, padx=5, pady=5, sticky="ne")
        #Sign Up Button
        self.SignUp_btn = ctk.CTkButton(self, text="Sign up", command=ToSignUp)
        self.SignUp_btn.grid(row=0, column=1, padx=5, pady=5, sticky="ne")