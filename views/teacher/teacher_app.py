""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
"""

import customtkinter as ctk
from ._dashboard import DashboardFrame
from ._calendar import CalendarFrame
from ._history import HistoryFrame
from ._settings import SettingFrame
from .. import init_app
import models.resources as res

ctk.set_appearance_mode("light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class StudentApp(ctk.CTk):

    def __init__(self, user_data: list):
      
        super().__init__()

        self.isMinimized = False

        # What is going on?
        self.user_data = user_data

        # Theme design, because I can't setup json file for custom theme installation using set_default_theme.
        self.THEME_GREEN = ("#95D5B2", "#081c15")
        self.THEME_DARKGREEN = ("#80B699", "#1F664D")
        self.DEFAULT = ('white', 'black')


        # load images with light and dark mode image
        """ File directory pathing for images """

        self.LogoImage = ctk.CTkImage(res.fetch_image(res.images.cvsu_consult_logo), size=(30, 30))
        self.HomeImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.home_dark), dark_image=res.fetch_image(res.images.nav_ico.home_light), size=(20, 20))
        self.CalendarImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.calendar_dark), dark_image=res.fetch_image(res.images.nav_ico.calendar_light), size=(20, 20))
        self.HistoryImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.history_dark), dark_image=res.fetch_image(res.images.nav_ico.history_light), size=(20, 20))
        self.SettingImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.settings_dark), dark_image=res.fetch_image(res.images.nav_ico.settings_light), size=(20, 20))
        self.MenuSliderImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.menu_dark), dark_image=res.fetch_image(res.images.nav_ico.menu_light), size=(20, 20))
        self.LogoutImage = ctk.CTkImage(light_image=res.fetch_image(res.images.nav_ico.logout_dark), dark_image=res.fetch_image(res.images.nav_ico.logout_light), size=(20, 20))

        """ End of resource pathing """

        # Window Configurations
        self.geometry(f"{res.constants.WIN_WIDTH}x{res.constants.WIN_HEIGHT}")
        self.title(f"CvSu Consult - Welcome back.")
        self.iconbitmap(res.images.window_icon)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Slide Panel | Navigation - Implementation and Configurations
        self.SlidePanel = ctk.CTkFrame(self, corner_radius=0, fg_color= self.THEME_GREEN)
        self.SlidePanel.grid(row=0, column=0, sticky="nsw")
        self.SlidePanel.grid_rowconfigure(1, weight=1)
        self.SlidePanel.grid_columnconfigure(1, weight=1)

        # Slide Panel | Burger as Label
        self.BurgerBtn = ctk.CTkButton(self.SlidePanel, text=None, image=self.MenuSliderImage, fg_color=self.THEME_GREEN, width=3, bg_color=self.THEME_GREEN, command=lambda: self.ToggleBurgerMenu())
        self.BurgerBtn.grid(row=0, column=0, sticky="e")

        # Slide Panel | Title as Label
        self.SlidePanelTitle = ctk.CTkLabel(self.SlidePanel, width=10, text=" CvSU Consult ", image=self.LogoImage, compound="left", font=ctk.CTkFont(size=15, weight="bold"))
        self.SlidePanelTitle.grid(row=1, column=0, padx=20, pady=20, sticky="nw")

        # Slide panel | Dashboard/Home Button
        self.ToDashboard = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Dashboard", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.HomeImage, anchor="w", command=lambda: self.SelectedPanel("dashboard"))
        self.ToDashboard.grid(row=2, column=0, sticky="ew")

        # Slide panel | Calendar Button
        self.ToCalendar = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Calendar", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.CalendarImage, anchor="w", command=lambda: self.SelectedPanel("calendar"))
        self.ToCalendar.grid(row=4, column=0, sticky="ew")

        # Slide panel | History Button
        self.ToHistory = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="History", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.HistoryImage, anchor="w", command=lambda: self.SelectedPanel("history"))
        self.ToHistory.grid(row=5, column=0, sticky="ew")

        # Slide panel | Settings Button
        self.ToSettings = ctk.CTkButton(self.SlidePanel, corner_radius=0, width=10, height=40, border_spacing=10, text="Settings", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), image=self.SettingImage, anchor="w", command=lambda: self.SelectedPanel("settings"))
        self.ToSettings.grid(row=6, column=0, sticky="ew")

        # Slide panel | Theme Dropdown
        self.ThemeMode = ctk.CTkOptionMenu(self.SlidePanel, values=["Light", "Dark"], command=lambda mode: ctk.set_appearance_mode(mode), fg_color=self.THEME_DARKGREEN, dropdown_fg_color=self.THEME_DARKGREEN, button_color=self.THEME_DARKGREEN, button_hover_color=self.THEME_DARKGREEN, text_color=("black", "white"))
        self.ThemeMode.grid(row=7, column=0, padx=5, pady=5, sticky="s")

        # Slide panel | Logout Button
        self.Logout = ctk.CTkButton(self.SlidePanel, image=self.LogoutImage, width=10, corner_radius=0, height=10, border_spacing=10, text="Logout", fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=lambda: self.logout_handler())
        self.Logout.grid(row=8, column=0, pady=5, padx=5, sticky="s")

        # Dashboard | Home Panel - Implementation and Configurations on ./_dashboard.py
        self.DashboardPanel = DashboardFrame(master=self, corner_radius=0, fg_color="transparent")
        # Calendar | Calendar Panel - Implementation and Configurations on ./_calendar.py
        self.CalendarPanel = CalendarFrame(master=self, corner_radius=0, fg_color="transparent")
        # Consultation | Consultation Panel - Implementation and Configurations on ./_consultation.py
        self.HistoryPanel = HistoryFrame(master=self, corner_radius=0, fg_color="transparent")
        # Settings | Settings Panel - Implementation and Configurations on ./_settings.py
        self.SettingsPanel = SettingFrame(master=self, corner_radius=0, fg_color="transparent")

        # Default Window Frame on load
        self.SelectedPanel("dashboard")

    #There's probably no proper way to achieve this in python
    def ToggleBurgerMenu(self):
        if(self.isMinimized):
            self.BurgerBtn.grid(row=0, column=0, sticky="e")
            self.SlidePanelTitle.configure(text=" CvSU Consult ", anchor="center")
            self.ToDashboard.configure(text="Dashboard", anchor="w")
            self.ToCalendar.configure(text="Calendar", anchor="w")
            self.ToHistory.configure(text="My History", anchor="w")
            self.ToSettings.configure(text="Settings", anchor="w")
            self.Logout.configure(text="Logout", anchor="w")
            self.Logout.grid(row=8, column=0, pady=5, padx=5, sticky="s")

            self.ThemeMode.configure(values=["Light", "Dark"])
            self.ThemeMode.grid(row=7, column=0, padx=5, pady=5, sticky="s")
            self.isMinimized = False
        else:
            self.BurgerBtn.grid(row=0, column=0, sticky="ew")
            self.SlidePanelTitle.configure(text="", anchor="center")
            self.ToDashboard.configure(text=None, anchor="center")
            self.ToCalendar.configure(text=None, anchor="center")
            self.ToHistory.configure(text=None, anchor="center")
            self.ToSettings.configure(text=None, anchor="center")
            self.Logout.configure(text=None, anchor="center")

            self.ThemeMode.configure(values=[])
            self.ThemeMode.grid_forget()
            self.isMinimized = True


    def logout_handler(self):
        self.destroy()
        init_app.init = init_app.App()
        init_app.init.mainloop()

    # method for changing panel views
    def SelectedPanel(self, name):

        # Clean selected frame on call
        frames = [self.ToDashboard, self.ToCalendar, self.ToHistory, self.ToSettings]
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

        if name == "calendar":
            # Display
            self.CalendarPanel.grid(row=0, column=1, sticky="nsew")
            # Show as "selected button"
            self.ToCalendar.configure(fg_color=("gray75", "gray25"))
        else:
            self.CalendarPanel.grid_forget()

        if name == "history":
            # Display
            self.HistoryPanel.grid(row=0, column=1, sticky="nsew")
            # Show as "selected button"
            self.ToHistory.configure(fg_color=("gray75", "gray25"))
        else:
            self.HistoryPanel.grid_forget()

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