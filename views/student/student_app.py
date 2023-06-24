""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_auth.py
"""

import customtkinter as ctk
import os
from PIL import Image

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class StudentApp(ctk.CTk):
    
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, user_data: list):
        super().__init__()

        # What is going on?
        self.user_data = user_data

        # Window Configurations
        self.title(f"Welcome, {self.user_data[3]}.")
        self.iconbitmap('./resources/images/window-icon.ico')
        self.geometry(f"{self.WIDTH}x{self.HEIGHT}")

        # Default Window Frame on load
        self.SelectedPanel("dashboard")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        """ File directory pathing for images
        Need image fixing, should use svg icons for icons due to resolution stretching when scaling. No error found.
        """
        image_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "..", "resources", "images"))

        self.logo_image = ctk.CTkImage(Image.open(os.path.join(image_path, "CvSU Consult Logo.png")), size=(30, 30))
        self.large_test_image = ctk.CTkImage(Image.open(os.path.join(image_path, "Poster.png")), size=(500, 150))
        self.image_icon_image = ctk.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(20, 20))
        self.add_user_image = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        """ End of resource pathing """
    
        # Slide Panel | Navigation - Implementation and Configurations
        self.SlidePanel = ctk.CTkFrame(self, corner_radius=0, fg_color=("#95D5B2", "#081c15"))
        self.SlidePanel.grid(row=0, column=0, sticky="nsew")
        self.SlidePanel.grid_rowconfigure(4, weight=1)

        # Slide Panel | Title as Label
        self.SlidePanelTitle = ctk.CTkLabel(self.SlidePanel, text="CvSU Consult", image=self.logo_image, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.SlidePanelTitle.grid(row=0, column=0, padx=20, pady=40, sticky="nw")

        # Slide panel | Dashboard/Home Button
        self.ToDashboard = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.home_image, anchor="w", command=self.home_button_event)
        self.ToDashboard.grid(row=1, column=0, sticky="ew")
        
        # Slide panel | Faculty Member Button
        self.ToFaculty = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Calendar", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.chat_image, anchor="w", command=self.frame_2_button_event)
        self.ToFaculty.grid(row=2, column=0, sticky="ew")

        # Slide panel | Consultations Button
        self.ToConsultation = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="My Consultations", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.ToConsultation.grid(row=3, column=0, sticky="ew")

        # Slide panel | Settings Button
        self.ToSettings = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
        self.ToSettings.grid(row=3, column=0, sticky="ew")

        # Slide panel | Theme Dropdown
        self.ThemeMode = ctk.CTkOptionMenu(self.SlidePanel, values=["Light", "Dark"], command=self.change_appearance_mode_event, fg_color="#2B9348")
        self.ThemeMode.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        

        # Dashboard | Home Panel - Implementation and Configurations
        self.HomePanel = ctk.CTkFrame(self, corner_radius=0, fg_color=("white", "black"))
        self.HomePanel.grid_columnconfigure(0, weight=1)

        # Faculty | Faculty Schedule Panel - Implementation and Configurations
        self.FacultyPanel = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FacultyPanel.grid(row=0, column=0, sticky="nsew")

        # Calendar | Calendar Panel - Implementation and Configurations
        self.Calendar = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Calendar.grid(row=0, column=0, sticky="nsew")

        # Consultation | Consultation Panel - Implementation and Configurations
        self.Consultation = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Consultation.grid(row=0, column=0, sticky="nsew")

        # Settings | Settings Panel - Implementation and Configurations
        self.Settings = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.Settings.grid(row=0, column=0, sticky="nsew")

    def SelectedPanel(self, name):
        # set button color for selected button
        self.ToDashboard.configure(fg_color=("gray75", "gray25") if name == "dashboard" else "transparent")
        self.ToFaculty.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.ToCalendar.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

        # show selected frame
        if name == "dashboard":
            self.HomePanel.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()
        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def second_frame_button_click(self):
        print("Second frame button clicked")


    def change_appearance_mode_event(self, new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)



# This is used to initialize the student application window in the login method -> ValidateUser
def _dangerouslyInit(user_data: list) -> None:
    app = StudentApp(user_data=user_data)
    app.mainloop()





if __name__ == "__main__":
    _dangerouslyInit([0, "admin", "admin", "adminadmin", "admin@gmail.com", "password", "S"])