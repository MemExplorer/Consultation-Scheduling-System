""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_init.py
"""

import customtkinter as ctk
import tkinter as tk

class DashboardFrame(ctk.CTkFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Dashboard title
        self.DashboardTitle = ctk.CTkLabel(self, text="DashboardPanel")
        self.DashboardTitle.grid(row=0, column=0, sticky = "nsew")