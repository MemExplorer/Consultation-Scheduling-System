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



        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image

        """ File directory pathing for images """
        image_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "..", "resources", "images"))
        slider_images = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "..", "resources", "images", "nav-icons"))

        self.LogoImage = ctk.CTkImage(Image.open(os.path.join(image_path, "CvSU Consult Logo.png")), size=(30, 30))
        self.HomeImage = ctk.CTkImage(light_image=Image.open(os.path.join(slider_images, "home-dark.png")), dark_image=Image.open(os.path.join(slider_images, "home-light.png")), size=(20, 20))
        self.FacultyImage = ctk.CTkImage(light_image=Image.open(os.path.join(slider_images, "faculty-dark.png")), dark_image=Image.open(os.path.join(slider_images, "faculty-light.png")), size=(20, 20))
        self.CalendarImage = ctk.CTkImage(light_image=Image.open(os.path.join(slider_images, "calendar-dark.png")), dark_image=Image.open(os.path.join(slider_images, "calendar-light.png")), size=(20, 20))
        self.ConsultationImage = ctk.CTkImage(light_image=Image.open(os.path.join(slider_images, "consultation-dark.png")), dark_image=Image.open(os.path.join(slider_images, "consultation-light.png")), size=(20, 20))
        self.SettingImage = ctk.CTkImage(light_image=Image.open(os.path.join(slider_images, "settings-dark.png")), dark_image=Image.open(os.path.join(slider_images, "settings-light.png")), size=(20, 20))

        """ End of resource pathing """
    
        # Slide Panel | Navigation - Implementation and Configurations
        self.SlidePanel = ctk.CTkFrame(self, corner_radius=0, fg_color=("#95D5B2", "#081c15"))
        self.SlidePanel.grid(row=0, column=0, sticky="nsew")
        self.SlidePanel.grid_rowconfigure(6, weight=1)

        # Slide Panel | Title as Label
        self.SlidePanelTitle = ctk.CTkLabel(self.SlidePanel, text=" CvSU Consult ", image=self.LogoImage, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.SlidePanelTitle.grid(row=0, column=0, padx=20, pady=40, sticky="nw")

        # Slide panel | Dashboard/Home Button
        self.ToDashboard = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.HomeImage, anchor="w", command=lambda: self.SelectedPanel("dashboard"))
        self.ToDashboard.grid(row=1, column=0, sticky="ew")
        
        # Slide panel | Faculty Member Button
        self.ToFaculty = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Faculty Schedules", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.FacultyImage, anchor="w", command=lambda: self.SelectedPanel("faculty"))
        self.ToFaculty.grid(row=2, column=0, sticky="ew")

        # Slide panel | Calendar Button
        self.ToCalendar = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Calendar", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.CalendarImage, anchor="w", command=lambda: self.SelectedPanel("calendar"))
        self.ToCalendar.grid(row=3, column=0, sticky="ew")

        # Slide panel | Consultations Button
        self.ToConsultation = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="My Consultations", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.ConsultationImage, anchor="w", command=lambda: self.SelectedPanel("consultation"))
        self.ToConsultation.grid(row=4, column=0, sticky="ew")

        # Slide panel | Settings Button
        self.ToSettings = ctk.CTkButton(self.SlidePanel, corner_radius=0, height=40, border_spacing=10, text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.SettingImage, anchor="w", command=lambda: self.SelectedPanel("settings"))
        self.ToSettings.grid(row=5, column=0, sticky="ew")

        # Slide panel | Theme Dropdown
        self.ThemeMode = ctk.CTkOptionMenu(self.SlidePanel, values=["Light", "Dark"], command=lambda mode: ctk.set_appearance_mode(mode), fg_color=("#80B699", "#1F664D"), dropdown_fg_color=("#80B699", "#1F664D"), button_color=("#80B699", "#1F664D"), button_hover_color=("#80B699", "#1F664D"), text_color=("black", "white"))
        self.ThemeMode.grid(row=6, column=0, padx=20, pady=20, sticky="s")
        

        # Dashboard | Home Panel - Implementation and Configurations
        self.DashboardPanel = ctk.CTkFrame(self, corner_radius=0, fg_color=("white", "black"))
        self.DashboardPanel.grid(row=0, column=0, sticky="nsew")
        self.DashboardTitle = ctk.CTkLabel(self.DashboardPanel, text="DashboardPanel")
        self.DashboardTitle.grid(row=0, column=0, sticky = "nsew")

        # Faculty | Faculty Schedule Panel - Implementation and Configurations
        self.FacultyPanel = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.FacultyPanel.grid(row=0, column=0, sticky="nsew")
        self.FacultyTitle = ctk.CTkLabel(self.FacultyPanel, text="FacultyPanel")
        self.FacultyTitle.grid(row=0, column=0, sticky = "nsew")

        # Calendar | Calendar Panel - Implementation and Configurations
        self.CalendarPanel = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.CalendarPanel.grid(row=0, column=0, sticky="nsew")
        self.CalendarTitle = ctk.CTkLabel(self.CalendarPanel, text="CalendarPanel")
        self.CalendarTitle.grid(row=0, column=0, sticky = "nsew")

        # Consultation | Consultation Panel - Implementation and Configurations
        self.ConsultationPanel = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ConsultationPanel.grid(row=0, column=0, sticky="nsew")
        self.ConsultationTitle = ctk.CTkLabel(self.ConsultationPanel, text="ConsultationPanel")
        self.ConsultationTitle.grid(row=0, column=0, sticky = "nsew")

        # Settings | Settings Panel - Implementation and Configurations
        self.SettingsPanel = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.SettingsPanel.grid(row=0, column=0, sticky="nsew")
        self.ConsultationTitle = ctk.CTkLabel(self.ConsultationPanel, text="ConsultationPanel")
        self.ConsultationTitle.grid(row=0, column=0, sticky = "nsew")

        # Default Window Frame on load
        self.SelectedPanel("dashboard")

    # method for changing panel views
    def SelectedPanel(self, name):

        # Clean selected frame on call
        frames = [self.ToDashboard, self.ToFaculty, self.ToCalendar, self.ToConsultation, self.ToSettings]
        for f in frames:
            f.configure(fg_color="transparent")

        # Display selected frame
        if name == "dashboard":
                # Display
                self.DashboardPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToDashboard.configure(fg_color=("gray75", "gray25"))
        else:
            self.DashboardPanel.grid_forget()

        if name == "faculty":
                # Display
                self.FacultyPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToFaculty.configure(fg_color=("gray75", "gray25"))
        else:
            self.FacultyPanel.grid_forget()

        if name == "calendar":
                # Display
                self.CalendarPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToCalendar.configure(fg_color=("gray75", "gray25"))
        else:
            self.CalendarPanel.grid_forget()

        if name == "consultation":
                # Display
                self.ConsultationPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToConsultation.configure(fg_color=("gray75", "gray25"))
        else:
            self.ConsultationPanel.grid_forget()

        if name == "settings":
                # Display
                self.SettingsPanel.grid(row=0, column=1, sticky="nsew")
                # Show as "selected button"
                self.ToSettings.configure(fg_color=("gray75", "gray25"))
        else:
            self.SettingsPanel.grid_forget()

# This is used to initialize the student application window in the login method -> ValidateUser
def _dangerouslyInit(user_data: list) -> None:
    app = StudentApp(user_data=user_data)
    app.mainloop()

if __name__ == "__main__":
    _dangerouslyInit([0, "admin", "admin", "adminadmin", "admin@gmail.com", "password", "S"])