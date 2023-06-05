from datetime import datetime
import customtkinter
import tkinter as tk  # Import tkinter for Toplevel
from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkEntry
from tkcalendar import DateEntry

# Set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Create main window
root = customtkinter.CTk()
root.geometry("500x350")

# Declare global variables for date_entry and time_entry
global date_entry, time_entry, logged_in_frame

def login():
    global date_entry, time_entry, logged_in_frame  # Access global variables

    username = entry1.get()
    password = entry2.get()

    if username == "admin" and password == "1":
        frame.destroy()

        # Create logged-in frame
        logged_in_frame = customtkinter.CTkFrame(master=root)
        logged_in_frame.pack(pady=50, padx=60, fill="both", expand=True)

        welcome_label = customtkinter.CTkLabel(master=logged_in_frame, text="Welcome, " + username)
        welcome_label.pack(pady=12, padx=10)

        # Create date selection
        date_label = customtkinter.CTkLabel(master=logged_in_frame, text="Date:")
        date_label.pack(pady=12, padx=10)
        date_entry = DateEntry(logged_in_frame, width=12, background='darkblue', foreground='white', borderwidth=2)
        date_entry.pack(pady=12, padx=10)

        # Create time selection
        time_label = customtkinter.CTkLabel(master=logged_in_frame, text="Time (HH:MM):")
        time_label.pack(pady=12, padx=10)
        time_entry = customtkinter.CTkEntry(master=logged_in_frame)
        time_entry.pack(pady=12, padx=10)

        now = datetime.now()
        date_entry.set_date(now.date())
        time_entry.insert(0, now.strftime("%H:%M"))

        # Create confirm button
        confirm_button = customtkinter.CTkButton(master=logged_in_frame, text="Confirm Schedule", command=confirm_schedule)
        confirm_button.pack(pady=12, padx=10)

    else:
        print("Invalid username or password")

def confirm_schedule():
    global date_entry, time_entry, logged_in_frame  # Access global variables

    selected_date = date_entry.get_date()
    selected_time = time_entry.get()

    # Display desired schedule
    schedule_label = customtkinter.CTkLabel(master=logged_in_frame, text="Desired Schedule")
    schedule_label.pack(pady=12, padx=10)

    date_label = customtkinter.CTkLabel(master=logged_in_frame, text="Date: " + str(selected_date))
    date_label.pack(pady=6, padx=10)

    time_label = customtkinter.CTkLabel(master=logged_in_frame, text="Time: " + selected_time)
    time_label.pack(pady=6, padx=10)

# Create login frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=50, padx=60, fill="both", expand=True)

# Create login form
label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

check = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
check.pack(pady=12, padx=10)

root.mainloop()