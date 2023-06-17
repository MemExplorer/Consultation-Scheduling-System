""" CTK Frame Module
This is a frame file. You can't run this file as a "__main__".
Reference frame for main_auth.py
"""

import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from tkcalendar import DateEntry

def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    window.geometry(f'{window_width}x{window_height}+{x}+{y}')

def display_name():
    teacher_name = name_input.get()
    text_editor.insert(tk.END, f"Teacher's name: {teacher_name}\n")

def display_date():
    selected_date = date_entry.get_date()
    text_editor.insert(tk.END, f"Selected date: {selected_date}\n")

window = ThemedTk(theme="arc")
window.title("Teacher Dashboard")
window.geometry('900x600')

name_label = ttk.Label(window, text="Teacher's Name:")
name_label.grid(column=0, row=0, padx=10, pady=10)

name_input = ttk.Entry(window)
name_input.grid(column=1, row=0, padx=10, pady=10)

name_button = ttk.Button(window, text="Display Name", command=display_name)
name_button.grid(column=2, row=0, padx=(50, 10), pady=10)

text_editor_label = ttk.Label(window, text="Scheduler:")
text_editor_label.grid(column=0, row=1, padx=10, pady=10)

text_editor = tk.Text(window, wrap=tk.WORD)
text_editor.grid(column=1, row=1, padx=10, pady=10)

date_entry_label = ttk.Label(window, text="Pick a date:")
date_entry_label.grid(column=0, row=2, padx=10, pady=10)

date_entry = DateEntry(window)
date_entry.grid(column=1, row=2, padx=10, pady=10)

date_button = ttk.Button(window, text="Display Date", command=display_date)
date_button.grid(column=2, row=2, padx=(50, 10), pady=10)

center_window(window)
# window.mainloop() - disabled due to runtime testing conflict.
