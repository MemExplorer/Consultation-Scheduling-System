""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import models.resources as res

class DashboardFrame(ctk.CTkFrame):

    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        
        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = self.master.THEME_GREEN
        self.THEME_DARKGREEN = self.master.THEME_DARKGREEN
        self.THEME_BLACK = self.master.THEME_BLACK
        self.THEME_WHITE = self.master.THEME_WHITE


        # load images with light and dark mode image
        """ File directory pathing for images """
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(70, 70))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(70, 70))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(70, 70))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        
        """ End of resource pathing """

        # Size of the scalable window
        self.WIDTH = self.master.WIDTH
        self.HEIGHT = self.master.HEIGHT

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = self.master.THEME_GREEN
        self.THEME_DARKGREEN = self.master.THEME_DARKGREEN
        self.THEME_BLACK = self.master.THEME_BLACK
        self.THEME_WHITE = self.master.THEME_WHITE


        # Dashboard wrapper for grouping the dashboard utilities
        self.DashWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.DashWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.DashWrapper.grid_columnconfigure(0, weight=1)

        # DashWrapper | Dashboard Welcome Message
        self.WelcomeLabel = ctk.CTkLabel(self.DashWrapper, text=f"Welcome, {self.user_data['username']}!", font=ctk.CTkFont(size=25))
        self.WelcomeLabel.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # DashWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.NotifImage, width=5, fg_color=self.THEME_GREEN)
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerDashWrapper = ctk.CTkFrame(self.DashWrapper, fg_color=self.THEME_DARKGREEN)
        self.InnerDashWrapper.grid(row=1, columnspan=5, padx=20, sticky="nsew")
        self.InnerDashWrapper.grid_columnconfigure(0, weight=1)
        self.InnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerInnerDashWrapper = ctk.CTkFrame(self.InnerDashWrapper, fg_color=self.THEME_DARKGREEN)
        self.InnerInnerDashWrapper.grid(row=0, column=0, padx=10)
        self.InnerInnerDashWrapper.grid_columnconfigure(1, weight=1)
        self.InnerInnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Yet another inner wrapper for containing navigations
        self.FacultyDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=self.THEME_GREEN)
        self.FacultyDashWrapper.grid(row=0, column=0, padx=30, pady=15)
        self.FacultyDashWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyDashWrapper.grid_rowconfigure(3, weight=1)

        # Yet another inner wrapper for containing navigations
        self.CalendarDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=self.THEME_GREEN)
        self.CalendarDashWrapper.grid(row=0, column=1, padx=30, pady=15)
        self.CalendarDashWrapper.grid_columnconfigure(0, weight=1)
        self.CalendarDashWrapper.grid_rowconfigure(3, weight=1)

        # Yet another inner wrapper for containing navigations
        self.ConsultationDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color=self.THEME_GREEN)
        self.ConsultationDashWrapper.grid(row=0, column=2, padx=30, pady=15)
        self.ConsultationDashWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationDashWrapper.grid_rowconfigure(3, weight=1)

        # Large Faculty Image
        self.FacultyDashImage = ctk.CTkLabel(self.FacultyDashWrapper, text=None, image=self.FacultyImage)
        self.FacultyDashImage.grid(row=0, column=0, padx=5, pady=5)
        # Faculty Label
        self.FacultyDashLabel = ctk.CTkLabel(self.FacultyDashWrapper, text="Faculty Schedule", font=ctk.CTkFont(size=13))
        self.FacultyDashLabel.grid(row=1, column=0, padx=5, pady=5)
        # Faculty Label
        self.FacultyDashButton = ctk.CTkButton(self.FacultyDashWrapper, text="View All", font=ctk.CTkFont(size=10), command=lambda: self.master.SelectedPanel('faculty'))
        self.FacultyDashButton.grid(row=2, column=0, padx=5, pady=5)

        # Large Calendar Image
        self.CalendarDashImage = ctk.CTkLabel(self.CalendarDashWrapper, text=None, image=self.CalendarImage)
        self.CalendarDashImage.grid(row=0, column=0, padx=5, pady=5)
        # Calendar Label
        self.CalendarDashLabel = ctk.CTkLabel(self.CalendarDashWrapper, text="Calendar History", font=ctk.CTkFont(size=13))
        self.CalendarDashLabel.grid(row=1, column=0, padx=5, pady=5)
        # Calendar Button
        self.CalendarDashButton = ctk.CTkButton(self.CalendarDashWrapper, text="View All", font=ctk.CTkFont(size=10), command=lambda: self.master.SelectedPanel('calendar'))
        self.CalendarDashButton.grid(row=2, column=0, padx=5, pady=5)

        # Large Consultation Image
        self.ConsultationDashImage = ctk.CTkLabel(self.ConsultationDashWrapper, text=None, image=self.ConsultationImage)
        self.ConsultationDashImage.grid(row=0, column=0, padx=5, pady=5)
        # Consultation Label
        self.ConsultationDashLabel = ctk.CTkLabel(self.ConsultationDashWrapper, text="My Consultation", font=ctk.CTkFont(size=13))
        self.ConsultationDashLabel.grid(row=1, column=0, padx=5, pady=5)
        # Consultation Button
        self.ConsultationDashButton = ctk.CTkButton(self.ConsultationDashWrapper, text="View All", font=ctk.CTkFont(size=10), command=lambda: self.master.SelectedPanel('consultation'))
        self.ConsultationDashButton.grid(row=2, column=0, padx=5, pady=5)

        # Upcoming Consultation wrapper for grouping the dashboard utilities
        self.ConWrapper = ctk.CTkFrame(master=self, fg_color=self.THEME_GREEN)
        self.ConWrapper.grid(row=1, columnspan=1, padx=20, pady=10, sticky="nsew")


        
