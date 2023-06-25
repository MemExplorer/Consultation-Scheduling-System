""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk
import models.resources as res

class DashboardFrame(ctk.CTkFrame):


    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        # user data defined by the master
        self.user_data = self.master.user_data

        # load images with light and dark mode image
        """ File directory pathing for images """
        self.FacultyImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.faculty_dark), dark_image=res.fetch_image(res.images.nav_ico.faculty_light), size=(80, 80))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(80, 80))
        self.ConsultationImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.consultation_dark), dark_image=res.fetch_image(res.images.nav_ico.consultation_light), size=(80, 80))
        self.NotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.notif_dark), dark_image=res.fetch_image(res.images.nav_ico.notif_light), size=(20, 20))
        self.AlertNotifImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.alert_notif_dark), dark_image=res.fetch_image(res.images.nav_ico.alert_notif_light), size=(20, 20))
        """ End of resource pathing """

        # Styling as row-stretch
        self.grid_columnconfigure(0, weight=5)
        self.grid_rowconfigure(1, weight=1)

        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = self.master.THEME_GREEN
        self.THEME_DARKGREEN = self.master.THEME_DARKGREEN
        self.DEFAULT = self.master.DEFAULT


        # Dashboard wrapper for grouping the dashboard utilities
        self.DashWrapper = ctk.CTkFrame(master=self, fg_color="transparent")
        self.DashWrapper.grid(row=0, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.DashWrapper.grid_columnconfigure(0, weight=1)

        # DashWrapper | Dashboard Welcome Message
        self.WelcomeLabel = ctk.CTkLabel(self.DashWrapper, text=f"Welcome, {self.user_data['username']}!", text_color="#2B9348", font=ctk.CTkFont(family="Poppins", size=24, weight='bold'))
        self.WelcomeLabel.grid(row=0, column=0, pady=20, padx=10, sticky="w")

        # DashWrapper | Notifications
        self.NotifIcon = ctk.CTkButton(self.DashWrapper, text=None, image=self.NotifImage, width=5, fg_color="transparent", hover_color="#Fdf0d5")
        self.NotifIcon.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerDashWrapper = ctk.CTkFrame(self.DashWrapper, fg_color="transparent")
        self.InnerDashWrapper.grid(row=1, columnspan=5, padx=0, sticky="nsew")
        self.InnerDashWrapper.grid_columnconfigure(0, weight=1)
        self.InnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Inner dashboard wrapper for grouping the dashboard utilities
        self.InnerInnerDashWrapper = ctk.CTkFrame(self.InnerDashWrapper, fg_color="transparent")
        self.InnerInnerDashWrapper.grid(row=0, column=0, padx=0)
        self.InnerInnerDashWrapper.grid_columnconfigure(1, weight=1)
        self.InnerInnerDashWrapper.grid_rowconfigure(0, weight=1)

        # Yet another inner wrapper for containing navigations
        self.FacultyDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color="#Fdf0d5", width=160, height=185, corner_radius=5)
        self.FacultyDashWrapper.grid(row=0, column=0, padx=20, pady=0)
        self.FacultyDashWrapper.grid_columnconfigure(0, weight=1)
        self.FacultyDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.CalendarDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color="#Fdf0d5")
        self.CalendarDashWrapper.grid(row=0, column=1, padx=20, pady=0)
        self.CalendarDashWrapper.grid_columnconfigure(0, weight=1)
        self.CalendarDashWrapper.grid_rowconfigure(3, weight=2)

        # Yet another inner wrapper for containing navigations
        self.ConsultationDashWrapper = ctk.CTkFrame(self.InnerInnerDashWrapper, fg_color="#Fdf0d5")
        self.ConsultationDashWrapper.grid(row=0, column=2, padx=20, pady=0)
        self.ConsultationDashWrapper.grid_columnconfigure(0, weight=1)
        self.ConsultationDashWrapper.grid_rowconfigure(3, weight=2)

        # Large Faculty Image
        self.FacultyDashImage = ctk.CTkLabel(self.FacultyDashWrapper, text=None, image=self.FacultyImage)
        self.FacultyDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Faculty Label
        self.FacultyDashLabel = ctk.CTkLabel(self.FacultyDashWrapper, text="Faculty Schedule", font=ctk.CTkFont(size=13, weight='bold'), text_color="#55A630")
        self.FacultyDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Faculty Label
        self.FacultyDashButton = ctk.CTkButton(self.FacultyDashWrapper, text="View All",command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.FacultyDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Calendar Image
        self.CalendarDashImage = ctk.CTkLabel(self.CalendarDashWrapper, text=None, image=self.CalendarImage)
        self.CalendarDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Calendar Label
        self.CalendarDashLabel = ctk.CTkLabel(self.CalendarDashWrapper, text="Calendar History", font=ctk.CTkFont(size=13, weight='bold'), text_color="#55A630")
        self.CalendarDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Calendar Button
        self.CalendarDashButton = ctk.CTkButton(self.CalendarDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.CalendarDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Large Consultation Image
        self.ConsultationDashImage = ctk.CTkLabel(self.ConsultationDashWrapper, text=None, image=self.ConsultationImage)
        self.ConsultationDashImage.grid(row=0, column=0, padx=5, pady=10)
        # Consultation Label
        self.ConsultationDashLabel = ctk.CTkLabel(self.ConsultationDashWrapper, text="My Consultation", font=ctk.CTkFont(size=13, weight='bold'), text_color="#55A630")
        self.ConsultationDashLabel.grid(row=1, column=0, padx=25, pady=0)
        # Consultation Button
        self.ConsultationDashButton = ctk.CTkButton(self.ConsultationDashWrapper, text="View All", command=lambda: self.master.SelectedPanel('faculty'), width=100, height=25, corner_radius=5, fg_color="#2B9348", hover_color="#55A630", font=ctk.CTkFont(size=12))
        self.ConsultationDashButton.grid(row=2, column=0, padx=7, pady=10)

        # Upcoming Consultation wrapper for grouping the dashboard utilities
        self.ConWrapper = ctk.CTkScrollableFrame(master=self, fg_color="transparent")
        self.ConWrapper.grid(row=1, columnspan=1, padx=20, pady=10, ipady=10, sticky="nsew")
        self.ConWrapper.grid_columnconfigure(0, weight=1)

        # ConWrapper | Upcoming Consultations Label
        self.UpcomingConsultationsLabel = ctk.CTkLabel(self.ConWrapper, text="Upcoming Consultations", text_color="#2B9348", font=ctk.CTkFont(family="Poppins", size=20, weight='bold'))
        self.UpcomingConsultationsLabel.grid(row=0, column=0, pady=20, padx=20, sticky="w")

        # ConWrapper | View Details Label
        self.ViewDetailsButton = ctk.CTkButton(self.ConWrapper, fg_color="transparent", bg_color="transparent",text="View Details", text_color="gray", font=ctk.CTkFont(family="Poppins", size=13, underline=True), command=lambda: self.master.SelectedPanel("consultation"), hover=None)
        self.ViewDetailsButton.grid(row=0, column=1, pady=20, padx=20, sticky="w")

        