""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
from views import init_app
from views.teacher import teacher_app
from views.student import student_app
from models.db_system import DBSystem
from models._cryptography import Security
import base64

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#Log In Frame class
class LogInFrame(ctk.CTkFrame):

    # Frame Methods
    def ToSignUp(self) -> None:
        self.destroy()

        # New instance created because of the destroy() destroying the defined value of SignIn_frame in the init_app
        _signupframe = init_app.SignUpFrame(master=init_app.init, fg_color="#161616")
        _signupframe.place(relx=0.5, rely=0.5, anchor="center")

    # Frame Methods
    def ToResetPass(self) -> None:
        self.destroy()

        
        

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        

        
        # Validate if user email and password is the same as the query data.    
        def ValidateUser(email: str, password: str) -> None:
            # Instances used in this method block
            self.auth_instance = DBSystem()
            self.crypt = Security()

            # Fetch user data from the database
            user_data = self.auth_instance.SearchUserByEmail(email=email)

            if user_data is False:
                self.err_label.configure(text="Email address doesn't exist")
            else:
                # Decrypt and compare the user's password with the provided password

                user_password = self.crypt.Decrypt(base64.b64decode(user_data[5]).decode())


                if user_password == password:
                    if user_data[-1] == 'S':

                        init_app.init.destroy()
                        
                        # Callable instance of the student class
                        student_app._dangerouslyInit(user_data=user_data)
                        
               

                    else:
                        init_app.init.destroy()
                        teacher_app._dangerouslyInit(user_data=user_data)
                        
                else:
                    self.err_label.configure(text="Username or password is incorrect.")

    
        #space 
        self.space1 = ctk.CTkLabel(self, text=" ")
        self.space1.grid(row=0, column=0, padx=0, pady=3)

        #Create Header
        self.header = ctk.CTkLabel(self, text="CvSU-Carmona Campus", text_color="#55A630", font=('Roboto', 13))
        self.header.grid(row=1, column=0, padx=120, pady=0, sticky="nsew")
        self.header = ctk.CTkLabel(self, text="Consultation Scheduling System", text_color="#55A630", font=('Roboto', 11))
        self.header.grid(row=2, column=0, padx=120, pady=0, sticky="nsew")

        #space
        self.space2 = ctk.CTkLabel(self, text=" ")
        self.space2.grid(row=3, column=0, padx=0, pady=10)

        #Welcome Greeting
        self.welcomeg = ctk.CTkLabel(self, text="Welcome!", text_color="#2B9348", font=ctk.CTkFont('Roboto', 16, weight='bold'))
        self.welcomeg.grid(row=4, column=0, padx=55, pady=10, sticky="w")
       
        #Email Label and Entry
        self.Email_lbl = ctk.CTkLabel(self, text="Email:", font=('Arial', 12))
        self.Email_lbl.grid(row=5, column=0, padx=55, pady=0, sticky="w")
        self.Email = ctk.CTkEntry(self, placeholder_text="Enter your Email", width=285)
        self.Email.grid(row=6, column=0, padx=10, pady=0)


        #Password Label and Entry
        self.Password_lbl = ctk.CTkLabel(self, text="Password:")
        self.Password_lbl.grid(row=7, column=0, padx=55, pady=0, sticky="w")
        self.Password = ctk.CTkEntry(self, placeholder_text="Enter your password", width= 285, show="*")
        self.Password.grid(row=8, column=0, padx=10, pady=0)

        #Forgot Password Label
        self.ForgotPass = ctk.CTkLabel(self, text="Forgot Password?", fg_color="transparent", text_color="black", font=ctk.CTkFont('Arial', 10, underline=True))
        self.ForgotPass.grid(row=9, column=0, padx=60, pady=0, sticky="e")
    

        #Remember Me CheckBox
        self.RememberMe = ctk.CTkCheckBox(self, text="Remember Me", checkbox_height=17, checkbox_width=17, border_width=2, corner_radius=1)
        self.RememberMe.grid(row=10, column=0, padx=55, pady=0, sticky="w")
        
        #space 
        self.space3 = ctk.CTkLabel(self, text=" ")
        self.space3.grid(row=11, column=0, padx=0, pady=7)

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Log In", fg_color="#2B9348", command=lambda: ValidateUser(self.Email.get(), self.Password.get()))
        self.LogIn_btn.grid(row=12, column=0, padx=5, pady=5)
        
        #space 
        self.space3 = ctk.CTkLabel(self, text=" ")
        self.space3.grid(row=13, column=0, padx=0, pady=4)

        #Sign Up Label
        self.SignUp = ctk.CTkButton(self, text="Don't have an account? Sign Up here", command=self.ToSignUp, fg_color="transparent", hover=False, text_color="black", font=ctk.CTkFont(underline=True))
        self.SignUp.grid(row=14, column=0, padx=10, pady=15)

        #space 
        self.space3 = ctk.CTkLabel(self, text=" ")
        self.space3.grid(row=15, column=0, padx=0, pady=1)
        
