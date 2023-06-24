""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import re
import base64
import tkinter as tk
from models._cryptography import Security
from models.db_system import DBSystem
from views import init_app

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class SignUpFrame(ctk.CTkFrame):

    # Methods defined
    def ToLogin(self):
        self.destroy()
        _LogIn_frame = init_app.LogInFrame(master=init_app.init, fg_color="#Fdf0d5")
        _LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Title Label
        self.titleLabel = ctk.CTkLabel(self, text="Create an Account", font=("Roboto", 40, "bold"), text_color=("black", "#2B9348"))
        self.titleLabel.grid(rowspan=1, columnspan=5, padx=10, pady=20, sticky="nsew")

                # Name Label
        self.err_label = ctk.CTkLabel(self, text=" ", text_color="red", font=("Roboto", 15))
        self.err_label.grid(row=2, columnspan=5, padx=5, pady=20, sticky="nsew")

        # Name Label
        self.firstNameLabel = ctk.CTkLabel(self, text="First Name", text_color=("black", "#2B9348"))
        self.firstNameLabel.grid(row=3, column=0, padx=10, pady=10)

        # Name Entry Field
        self.firstNameEntry = ctk.CTkEntry(self, placeholder_text="John")
        self.firstNameEntry.grid(row=3, column=1, padx=10, pady=10)

        # Last Name Label
        self.lastNameLabel = ctk.CTkLabel(self, text="Last Name", text_color=("black", "#2B9348"))
        self.lastNameLabel.grid(row=3, column=2, padx=10, pady=10)

        # Last Name Entry Field
        self.lastNameEntry = ctk.CTkEntry(self, placeholder_text="Doe")
        self.lastNameEntry.grid(row=3, column=3, padx=10, pady=10)

        # Username Label
        self.usernameLabel = ctk.CTkLabel(self, text="Username", text_color=("black", "#2B9348"))
        self.usernameLabel.grid(row=4, column=0, padx=10, pady=10)

        # Username Field
        self.usernameEntry = ctk.CTkEntry(self, placeholder_text="John Doe")
        self.usernameEntry.grid(row=4, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Email Label
        self.emailLabel = ctk.CTkLabel(self, text="Email", text_color=("black", "#2B9348"))
        self.emailLabel.grid(row=5, column=0, padx=10, pady=10)

        # Email Entry Field
        self.emailEntry = ctk.CTkEntry(self, placeholder_text="example@example.com")
        self.emailEntry.grid(row=5, column=1, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Password Label
        self.passwordLabel = ctk.CTkLabel(self, text="Password", text_color=("black", "#2B9348"))
        self.passwordLabel.grid(row=6, column=0, padx=10, pady=10)

        # Password Entry Field
        self.passwordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Password")
        self.passwordEntry.grid(row=6, column=1, padx=10, pady=10)

        # Confirm Password Label
        self.confirmPasswordLabel = ctk.CTkLabel(self, text="Confirm Password", text_color=("black", "#2B9348"))
        self.confirmPasswordLabel.grid(row=6, column=2, padx=10, pady=10)

        # Confirm Password Entry Field
        self.confirmPasswordEntry = ctk.CTkEntry(self, show="*", placeholder_text="Confirm Password")
        self.confirmPasswordEntry.grid(row=6, column=3, padx=10, pady=10)


        # Role Label
        self.roleLabel = ctk.CTkLabel(self, text="Role", text_color=("black", "#2B9348"))
        self.roleLabel.grid(row=8, column=0, padx=10, pady=10)

        # Role Radio Buttons
        self.roleVar = tk.StringVar(value="Student")

        self.teacherRadioButton = ctk.CTkRadioButton(self, text="Teacher", variable=self.roleVar, value="Teacher", text_color=("black", "#2B9348"))
        self.teacherRadioButton.grid(row=8, column=1, padx=10, pady=10)

        self.studentRadioButton = ctk.CTkRadioButton(self, text="Student", variable=self.roleVar, value="Student", text_color=("black", "#2B9348"))
        self.studentRadioButton.grid(row=8, column=2, padx=10, pady=10)

        # Confirm Button
        self.confirmButton = ctk.CTkButton(self, text="Confirm", command=self.confirm, bg_color=("#2B9348", "#2B9348"), fg_color=("#2B9348", "#2B9348"), hover=("#2B9348", "#2B9348"))
        self.confirmButton.grid(row=9, columnspan=4, padx=10, pady=50, sticky="nsew")
        
        #Sign Up Label
        self.SignUp = ctk.CTkButton(self, text="Already have an account? Login here.", command=self.ToLogin, fg_color="transparent", hover=False, text_color=("black", "#2B9348"), font=ctk.CTkFont(underline=True))
        self.SignUp.grid(row=10, columnspan=5, padx=5, pady=10, sticky="nsew")

    # Frame Methods
    def confirm(self) -> None:

        # Create an instance for this method
        _dbsystem = DBSystem()
        _crypt = Security()

        # regex expression for email validation
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

        # Lambda expressions for simple functions needed for this method
        get_role = lambda: "S" if self.roleVar.get() == "Student" else "T"
        format_str = lambda: (fname.title(), lname.title(), username.title())
        check_if_existing_username = lambda: False if _dbsystem.SearchIfExistsByUsername(username=username) else True
        valid_email = lambda: True if re.fullmatch(regex, email) else False
        not_existing_email = lambda: True if _dbsystem.SearchIfExistsByEmail(email=email) else True

        fname = self.firstNameEntry.get()
        lname = self.lastNameEntry.get()
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        cpass = self.confirmPasswordEntry.get()
        email = self.emailEntry.get()
        role = get_role()

        # Format String Completion
        format_str()
        
        # Check if all fields are filled.
        not_Empty = (fname != '' and lname != '' and username != '' and password != '')
        password_Matched = (password == cpass)
        isValid_Email = (valid_email() and not_existing_email)
        isExisting_User = check_if_existing_username()
        valid_account = (not_Empty and isExisting_User and password_Matched and email != '' and isValid_Email)

        if not not_Empty:
            self.err_label.configure(text="Fields are empty.")
        elif not password_Matched:
            self.err_label.configure(text="Password fields do not match.")
        elif not isValid_Email:
            self.err_label.configure(text="Not a valid email address.")
        elif not isExisting_User:
            self.err_label.configure(text="Username already exists.")

        if valid_account:
            # Remove error label
            self.err_label.configure(text=" ")

            # Password encryption algorithms defined in _cryptography.py
            fernet_encryption = _crypt.Encrypt(password)
            base64_encryption = base64.b64encode(fernet_encryption).decode()

            # Commit to the database
            _dbsystem.RegisterUserAccount(fname=fname, lname=lname, username=username, email=email, password=base64_encryption, role=role)
            print(_dbsystem.QueryAccountData())

            # Redirecting to the login frame
            self.ToLogin()

