""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("Dark")  # Change appearance mode to "Dark"
ctk.set_default_color_theme("blue")  # Change color theme to "blue"

appWidth, appHeight = 600, 700

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Sign Up")
        self.geometry(f"{appWidth}x{appHeight}")

        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Sign Up", font=("Roboto", 24, "bold"))
        self.titleLabel.place(relx=0.5, rely=0.1, anchor="center")

        # Name Label
        self.nameLabel = ctk.CTkLabel(self, text="Name")
        self.nameLabel.place(relx=0.5, rely=0.2, anchor="center")

        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self, placeholder_text="Teja")
        self.nameEntry.place(relx=0.5, rely=0.25, anchor="center")

        # Password Label
        self.passwordLabel = ctk.CTkLabel(self, text="Password")
        self.passwordLabel.place(relx=0.5, rely=0.35, anchor="center")

        # Password Entry Field
        self.passwordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEntry.place(relx=0.5, rely=0.4, anchor="center")

        # Email Label
        self.emailLabel = ctk.CTkLabel(self, text="Email")
        self.emailLabel.place(relx=0.5, rely=0.5, anchor="center")

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.place(relx=0.5, rely=0.55, anchor="center")

        # Role Label
        self.roleLabel = ctk.CTkLabel(self, text="Role")
        self.roleLabel.place(relx=0.5, rely=0.65, anchor="center")

        # Role Radio Buttons
        self.roleVar = tk.StringVar(value="Student")

        self.teacherRadioButton = ctk.CTkRadioButton(self, text="Teacher", variable=self.roleVar, value="Teacher")
        self.teacherRadioButton.place(relx=0.4, rely=0.7, anchor="center")

        self.studentRadioButton = ctk.CTkRadioButton(self, text="Student", variable=self.roleVar, value="Student")
        self.studentRadioButton.place(relx=0.6, rely=0.7, anchor="center")

        # Confirm Button
        self.confirmButton = ctk.CTkButton(self, text="Confirm", command=self.confirm)
        self.confirmButton.place(relx=0.5, rely=0.8, anchor="center")

    def confirm(self):
        name = self.nameEntry.get()
        password = self.passwordEntry.get()
        email = self.emailEntry.get()
        role = self.roleVar.get()
        print(f"Name: {name}, Password: {password}, Email: {email}, Role: {role}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
