""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from PIL import ImageTk, Image
import os

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Log In Frame class
class LogInFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Destroys the Log In module, and opens the Main module
        def button_event():
            pass # No function yet

        #space 
        self.spaces = ctk.CTkLabel(self, text=" ")
        self.spaces.grid(row=0, column=0, padx=0, pady=3)

        #Create Header
        self.header = ctk.CTkLabel(self, text="CvSU-Carmona Campus", font=('Arial', 17))
        self.header.grid(row=1, column=0, padx=50, pady=0, sticky="nsew")
        self.header = ctk.CTkLabel(self, text="Consultation Scheduling System", font=('Arial', 15))
        self.header.grid(row=2, column=0, padx=50, pady=0, sticky="nsew")

        #Space
        self.spaces1 = ctk.CTkLabel(self, text=" ")
        self.spaces1.grid(row=3, column=0, padx=0, pady=3)

        #Email Label and Entry
        self.Email_lbl = ctk.CTkLabel(self, text="Email:", font=('Arial', 12))
        self.Email_lbl.grid(row=4, column=0, padx=55, pady=0, sticky="w")
        self.Email = ctk.CTkEntry(self, placeholder_text="Enter your Email", width=200)
        self.Email.grid(row=5, column=0, padx=10, pady=0)

        #Password Label and Entry
        self.Password_lbl = ctk.CTkLabel(self, text="Password:")
        self.Password_lbl.grid(row=6, column=0, padx=55, pady=0, sticky="w")
        self.Password = ctk.CTkEntry(self, placeholder_text="Enter your password", width=200, show="*")
        self.Password.grid(row=7, column=0, padx=10, pady=0)
        self.ForgotPass = ctk.CTkLabel(self, text="Forgot Password?", font=('Arial', 10))
        self.ForgotPass.grid(row=8, column=0, padx=55, pady=0, sticky="e")
        
        #User OptionMenu
        self.Users = ctk.CTkOptionMenu(self, values=["Student", "Faculty"])
        self.Users.grid(row=9, column=0, pady=10, padx=10)
        self.Users.set("User")

        #Remember Me CheckBox
        self.RememberMe = ctk.CTkCheckBox(self, text="Remember Me", checkbox_height=17, checkbox_width=17, border_width=2, corner_radius=1)
        self.RememberMe.grid(row=10, column=0, padx=55, pady=0, sticky="w")
        
        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Log In", command=button_event)
        self.LogIn_btn.grid(row=11, column=0, padx=10, pady=15)
        
        #Sign Up Label
        self.SignUp = ctk.CTkLabel(self, text="Don't have an account? Sign Up here.")
        self.SignUp.grid(row=12, column=0, padx=10, pady=15)

