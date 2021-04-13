# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Whack A Mole - USER SETTINGS
# I did not copy anyone

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import json
import os


# Needs a math function to determine rows/columns

class Settings:
    def __init__(self, arg):
        self.filename = 'WAMsettings.json'
        self.json_default = {"num_moles": 9,
                             "min_under": 1,
                             "max_under": 5,
                             "min_above": 1,
                             "max_above": 3,
                             "time": 30}

        self.win = tk.Tk()
        self.win.title("Game Settings")
        self.win.geometry('300x300')
        self.win.minsize(250, 225)
        config = [0, 1, 2, 3, 4, 5, 6, 7]
        self.win.columnconfigure([0, 1], weight=1, minsize=50)
        self.win.rowconfigure(config, weight=1, minsize=10)

        self.labels = ['Number of Moles:', 'Min time underground:', 'Max time underground:',
                       'Min time above ground:', 'Max time above ground:', 'Game time (seconds):']
        self.json_keys = ['num_moles', 'min_under', 'max_under', 'min_above', 'max_above', 'time']

        self.data_values = []
        self.entries = []
        self.p_data = {}
        self.final_data = {}

        if os.path.exists(self.filename):
            with open(self.filename) as f:
                self.data = json.load(f)
        else:
            self.data = self.json_default

        if arg:
            self.settings_screen()
        if not arg:
            self.no_screen()

    def save(self):
        saved_settings = []
        for _ in self.entries:
            try:
                saved_settings.append(int(_.get()))
            except ValueError:
                tk.messagebox.showerror("Error", "Please input whole numbers")
                return

        for idx, _ in enumerate(self.json_keys):
            self.p_data[_] = saved_settings[idx]

        if not saved_settings == self.data_values:
            with open(self.filename, 'w') as f:
                json.dump(self.p_data, f, indent=4)

        self.final_data = self.p_data

        if os.path.exists(self.filename):
            if self.p_data == self.json_default:
                os.remove('WAMsettings.json')

        self.win.destroy()

    def settings_screen(self):
        for _ in self.json_keys:
            self.data_values.append(self.data[_])

        for n in range(len(self.labels)):
            tk.Label(text=self.labels[n]).grid(row=n, column=0, sticky=tk.E)

            e = tk.StringVar()
            self.entries.append(tk.Entry(width=5, textvariable=e))
            self.entries[n].grid(row=n, column=1, sticky=tk.W, padx=10)
            e.set(self.data_values[n])

        btn = ttk.Button(self.win, text='Next', command=self.save)
        btn.place(relx=.5, rely=0.9, anchor=CENTER)

        self.win.mainloop()

    def no_screen(self):
        for _ in self.json_keys:
            self.data_values.append(self.data[_])

        for idx, _ in enumerate(self.json_keys):
            self.final_data[_] = self.data_values[idx]


if __name__ == '__main__':
    screen_bool = True
    settings = Settings(screen_bool)
    print(settings.final_data)
