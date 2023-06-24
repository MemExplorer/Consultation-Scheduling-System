""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res

class DashboardFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        """ File directory pathing for images """

        self.LogoImage = ctk.CTkImage(res.fetch_image(res.images.cvsu_consult_logo), size=(30, 30))
        self.HomeImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.home_dark), dark_image=res.fetch_image(res.images.nav_ico.home_light), size=(20, 20))
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(20, 20))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(20, 20))
        self.SettingImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.settings_dark), dark_image=res.fetch_image(res.images.nav_ico.settings_light), size=(20, 20))

        """ End of resource pathing """

        # Dashboard title
        self.DashboardTitle = ctk.CTkLabel(self, text="DashboardPanel")
        self.DashboardTitle.grid(row=0, column=0, sticky = "nsew")
