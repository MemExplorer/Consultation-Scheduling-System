import customtkinter as ctk
from login import LogInFrame

# Class inside the window space
class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        #Python Routing Methods
        def ToLogin():
            self.destroy()
            app.configure(fg_color="pink")
            app.LogIn_frame.place(relx=0.5, rely=0.5, anchor="center")

        def ToSignUp():
            app.destroy()

        #Log In Button
        self.LogIn_btn = ctk.CTkButton(self, text="Login", command=ToLogin)
        self.LogIn_btn.grid(row=14, column=0, padx=10, pady=15)

        #Sign Up Button
        self.SignUp_btn = ctk.CTkButton(self, text="Sign up", command=ToSignUp)
        self.SignUp_btn.grid(row=14, column=1, padx=10, pady=15)




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

        #Configure Log In Frame
        self.LogIn_frame = LogInFrame(master=self)
        self.LogIn_frame.configure(fg_color="white")

app = App()

# On instance run as main file. To test the program file only, not accessible as a module reference.
if __name__ == "__main__":
    app.mainloop()