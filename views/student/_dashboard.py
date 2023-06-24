""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import os
from PIL import ImageTk, Image

class DashboardFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """ File directory pathing for images """

        image_path = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "..", "resources", "images"))
        nav_icons = os.path.abspath(os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "..", "resources", "images", "nav-icons"))

        self.LogoImage = ctk.CTkImage(Image.open(os.path.join(image_path, "CvSU Consult Logo.png")), size=(30, 30))
        self.HomeImage = ctk.CTkImage(light_image=Image.open(os.path.join(nav_icons, "home-dark.png")), dark_image=Image.open(os.path.join(nav_icons, "home-light.png")), size=(20, 20))
        self.FacultyImage = ctk.CTkImage(light_image=Image.open(os.path.join(nav_icons, "faculty-dark.png")), dark_image=Image.open(os.path.join(nav_icons, "faculty-light.png")), size=(20, 20))
        self.CalendarImage = ctk.CTkImage(light_image=Image.open(os.path.join(nav_icons, "calendar-dark.png")), dark_image=Image.open(os.path.join(nav_icons, "calendar-light.png")), size=(20, 20))
        self.ConsultationImage = ctk.CTkImage(light_image=Image.open(os.path.join(nav_icons, "consultation-dark.png")), dark_image=Image.open(os.path.join(nav_icons, "consultation-light.png")), size=(20, 20))
        self.SettingImage = ctk.CTkImage(light_image=Image.open(os.path.join(nav_icons, "settings-dark.png")), dark_image=Image.open(os.path.join(nav_icons, "settings-light.png")), size=(20, 20))

        """ End of resource pathing """

        # Dashboard title
        self.DashboardTitle = ctk.CTkLabel(self, text="DashboardPanel")
        self.DashboardTitle.grid(row=0, column=0, sticky = "nsew")
