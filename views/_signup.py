""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk


class SignUpFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Sign Up", font=("Roboto", 24, "bold"))
        self.titleLabel.grid(rowspan=1, columnspan=5, padx=10, pady=50, sticky="nsew")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self, text="Name")
        self.nameLabel.grid(row=1, column=0, padx=10, pady=10)

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Teja")
        self.nameEntry.grid(row=1, column=1, padx=10, pady=10)

        # Password Label
        self.passwordLabel = ctk.CTkLabel(self, text="Password")
        self.passwordLabel.grid(row=2, column=0, padx=10, pady=10)

        # Password Entry Field
        self.passwordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEntry.grid(row=2, column=1, padx=10, pady=10)

        # Email Label
        self.emailLabel = ctk.CTkLabel(self, text="Email")
        self.emailLabel.grid(row=3, column=0, padx=10, pady=10)

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.grid(row=3, column=1, padx=10, pady=10)

        # Role Label
        self.roleLabel = ctk.CTkLabel(self, text="Role")
        self.roleLabel.grid(row=4, column=0, padx=10, pady=10)

        # Role Radio Buttons
        self.roleVar = tk.StringVar(value="Student")

        self.teacherRadioButton = ctk.CTkRadioButton(self, text="Teacher", variable=self.roleVar, value="Teacher")
        self.teacherRadioButton.grid(row=4, column=1, padx=10, pady=10)

        self.studentRadioButton = ctk.CTkRadioButton(self, text="Student", variable=self.roleVar, value="Student")
        self.studentRadioButton.grid(row=4, column=2, padx=10, pady=10)

        # Confirm Button
        self.confirmButton = ctk.CTkButton(self, text="Confirm", command=self.confirm)
        self.confirmButton.grid(row=5, columnspan=4, padx=10, pady=10, sticky="nsew")

    # Frame Methods
    def confirm(self):
        name = self.nameEntry.get()
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        role = self.roleVar.get()
        print(f"Name: {name}, Password: {password}, Email: {email}, Role: {role}")
