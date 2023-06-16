""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import re
import tkinter as tk
from models.cryptography import Security
from models.db_system import DBSystem

class SignUpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        # Frame Methods
        def RegisterUser() -> None:
            self.register_name = self.nameEntry.get()
            print(f"{self.register_name}")

        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Sign Up", font=("Roboto", 60, "bold"), text_color="white")
        self.titleLabel.grid(rowspan=1, columnspan=5, padx=10, pady=50, sticky="nsew")

        # Name Label
        self.firstNameLabel = ctk.CTkLabel(self, text="First Name", text_color="white")
        self.firstNameLabel.grid(row=1, column=0, padx=10, pady=10)

        # Name Entry Field
        self.firstNameEntry = ctk.CTkEntry(self, placeholder_text="John")
        self.firstNameEntry.grid(row=1, column=1, padx=10, pady=10)

        # Password Label
        self.passwordLabel = ctk.CTkLabel(self, text="Password", text_color="white")
        self.passwordLabel.grid(row=4, column=0, padx=10, pady=10)

        # Last Name Label
        self.lastNameLabel = ctk.CTkLabel(self, text="Last Name", text_color="white")
        self.lastNameLabel.grid(row=1, column=2, padx=10, pady=10)

        # Last Name Entry Field
        self.lastNameEntry = ctk.CTkEntry(self, placeholder_text="Doe")
        self.lastNameEntry.grid(row=1, column=3, padx=10, pady=10)

        # Username Label
        self.usernameLabel = ctk.CTkLabel(self, text="Username", text_color="white")
        self.usernameLabel.grid(row=2, column=0, padx=10, pady=10)

        # Name Entry Field
        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="John Doe")
        self.usernameEntry.grid(row=2, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Confirm Password Label
        self.confirmPasswordLabel = ctk.CTkLabel(self, text="Confirm Password", text_color="white")
        self.confirmPasswordLabel.grid(row=4, column=2, padx=10, pady=10)

        # Confirm Password Entry Field
        self.confirmPasswordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Confirm Password")
        self.confirmPasswordEntry.grid(row=4, column=3, padx=10, pady=10)


        # Password Entry Field
        self.passwordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEntry.grid(row=4, column=1, padx=10, pady=10)

        # Email Label
        self.emailLabel = ctk.CTkLabel(self, text="Email", text_color="white")
        self.emailLabel.grid(row=3, column=0, padx=10, pady=10)

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.grid(row=3, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Role Label
        self.roleLabel = ctk.CTkLabel(self, text="Role", text_color="white")
        self.roleLabel.grid(row=5, column=0, padx=10, pady=10)

        # Role Radio Buttons
        self.roleVar = tk.StringVar(value="Student")

        self.teacherRadioButton = ctk.CTkRadioButton(self, text="Teacher", variable=self.roleVar, value="Teacher", text_color="white")
        self.teacherRadioButton.grid(row=5, column=1, padx=10, pady=10)

        self.studentRadioButton = ctk.CTkRadioButton(self, text="Student", variable=self.roleVar, value="Student", text_color="white")
        self.studentRadioButton.grid(row=5, column=2, padx=10, pady=10)

        # Confirm Button
        self.confirmButton = ctk.CTkButton(self, text="Confirm", command=self.confirm)
        self.confirmButton.grid(row=6, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Frame Methods
    def confirm(self) -> None:

        # Create an instance for this method
        _dbsystem = DBSystem()
        _crypt = Security()

        # regex expression for email validation
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        # Lambda expressions for simple functions needed for this method
        get_role = lambda: "S" if self.roleVar.get() == "Student" else "T"
        valid_email = lambda: True if re.fullmatch(regex, email) else False

        fname = self.firstNameEntry.get()
        lname = self.lastNameEntry.get()
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        cpass = self.confirmPasswordEntry.get()
        email = self.emailEntry.get()
        role = get_role()



        isData_Filled = (fname != '' and lname != '' and username != '' and password != '' and password == cpass and email != '' and valid_email())

        print(valid_email())
        print(isData_Filled)

        if isData_Filled:

            # Password encryption
            crypted_pass = _crypt.Encrypt(password)

            # Commit to the database
            _dbsystem.RegisterUserAccount(fname=fname,lname=lname, username=username, email=email, password=crypted_pass, role=role)
            print(_dbsystem.QueryAccountData())