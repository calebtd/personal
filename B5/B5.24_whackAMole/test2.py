from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import json
import os


class Settings:
    def __init__(self, arg):
        self.json_default = {"num_moles": 9,
                             "min_under": 1,
                             "max_under": 5,
                             "min_above": 1,
                             "max_above": 1,
                             "time": 20}

        self.label_key = (('Number of Moles:', 'num_moles'), ('Min time underground:', 'min_under'),
                          ('Max time underground:', 'max_under'), ('Min time above ground:', 'min_above'),
                          ('Max time above ground:', 'max_above'), ('Game time (seconds):', 'time'))

        self.filename = 'WAMsettings.json'
        if os.path.exists(self.filename):
            with open(self.filename) as f:
                try:
                    self.data = json.load(f)
                except json.JSONDecodeError:
                    print('Error loading JSON, using default values')
                    self.data = self.json_default
        else:
            self.data = self.json_default

        self.final_data = {}
        self.entries = []
        self.win = None

        if arg:
            self.gui()
        elif not arg:
            self.no_gui()

    def gui(self):
        self.win = Tk()
        self.win.title('Game Settings')
        self.win.geometry('300x300')
        self.win.minsize(290, 290)
        self.win.maxsize(320, 320)
        # self.win.config(bg='black')
        frame = Frame(self.win)
        frame.pack(padx=5, pady=5)

        for x, y in enumerate(self.label_key):
            Label(frame, text=y[0], width=19, anchor=E).grid(row=x, column=0, padx=6)

            z = Entry(frame, width=5)

            try:
                z.insert(0, self.data[y[1]])
            except KeyError:
                print(f"Error loading '{y[1]}'. Using default value")
                z.insert(0, self.json_default[y[1]])

            z.grid(row=x, column=1, padx=6, pady=10)
            self.entries.append(z)

        ttk.Button(self.win, text='Save', command=self.save).place(relx=.5, rely=0.9, anchor=CENTER)

        self.win.mainloop()

    def no_gui(self):
        self.final_data = self.data
        if self.final_data == self.json_default:
            if os.path.exists(self.filename):
                os.remove(self.filename)

    def save(self):
        for x, y in enumerate(self.entries):
            try:
                self.final_data[self.label_key[x][1]] = int(y.get())
            except ValueError:
                messagebox.showerror('Error', 'Please input whole numbers')
                return

        print(self.final_data == self.json_default)
        if self.final_data == self.json_default:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        else:
            with open(self.filename, 'w') as f:
                json.dump(self.final_data, f, indent=4)
        self.win.destroy()
        print('RUN GAME')


if __name__ == '__main__':
    settings = Settings(False)
    print(settings.final_data)
