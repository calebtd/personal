# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Whack A Mole - FINAL PROGRAM
# I did not copy anyone

from random import randint
from time import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from math import *
import json
import os


# This is my Whack-a-mole full project. When it runs, it opens the welcome screen. From there you can either
# start the game right away, or change the settings before you start. Then it runs the gameplay. Once you win
# or lose, it will ask if you want to play again.

# I create three classes in the program. One for the Welcome screen, one for the Settings with or
# without a GUI, and one for the actual gameplay. The program only calls Welcome() at the bottom, and it
# references the rest of the classes within the code.

# The welcome screen runs the settings class when you hit a button, with a bool as a param.

# The settings class takes that bool to run with a GUI or not. If a settings file exists, it will scrape
# the data and use that as the settings. Otherwise it will use the default values. When you hit save on
# the GUI, it grabs the data you set and saves it to a file IF it's different than the default values
# It then runs the gameplay with the final settings data

# The game class builds a grid, adds labels with the mole images, and starts the timer.

class Welcome:
    def __init__(self):
        self.win = Tk()
        self.win.title("Whack-a-Mole")
        self.win.config(bg='black')

        frame1 = Frame(self.win, bg='black')
        frame2 = Frame(self.win, bg='black')
        frame1.pack()
        frame2.pack()

        Label(frame1, text="Welcome to \nWhack-a-Mole",
              font=('Bahnschrift', 50), fg='white', bg='black').pack()
        Label(frame1, height=5, bg='black').pack()

        for x, y in enumerate(('Settings', 'Start')):
            z = Button(frame2, text=y, font=('Bahnschrift', 15), fg='white', bg='black', activeforeground='white',
                       activebackground='grey', width=12, height=2, relief='ridge')
            z.config(command=lambda i=x: self.close(i))
            z.grid(row=2, column=x, padx=10, pady=10)
            z.bind("<Enter>", self.on_enter)
            z.bind("<Leave>", self.on_leave)
        self.win.mainloop()

    def close(self, btn):
        self.win.destroy()
        if btn == 0:
            Settings(True)
        elif btn == 1:
            Settings(False)

    @staticmethod
    def on_enter(btn):
        btn.widget.config(relief='sunken')

    @staticmethod
    def on_leave(btn):
        btn.widget.config(relief='ridge')


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
        Game(self.final_data)

    def save(self):
        for x, y in enumerate(self.entries):
            try:
                self.final_data[self.label_key[x][1]] = int(y.get())
            except ValueError:
                messagebox.showerror('Error', 'Please input whole numbers')
                return
            if self.final_data['num_moles'] > 32:
                messagebox.showerror('Error', 'Please input 32 moles or less')
                return

        if self.final_data == self.json_default:
            if os.path.exists(self.filename):
                os.remove(self.filename)
        else:
            with open(self.filename, 'w') as f:
                json.dump(self.final_data, f, indent=4)
        self.win.destroy()
        Game(self.final_data)


class Game:
    def __init__(self, settings_dict):
        self.data = settings_dict
        self.win = Tk()
        self.win.title("Whack-a-Mole")

        image0 = PhotoImage(file="sprite_0.png")
        image1 = PhotoImage(file="sprite_1.png")
        image2 = PhotoImage(file="sprite_2.png")
        self.image_list = [image0, image1, image2]

        self.timeText = StringVar()
        self.timer_time = self.data['time']
        self.timeText.set(f'Time: {self.timer_time}')

        frame1 = Frame(self.win)
        frame2 = Frame(self.win, bg='#D3D3D3', padx=1, pady=1)
        frame1.pack()
        frame2.pack(padx=10, pady=10)

        Label(frame1, font=('Bahnschrift', 40), textvariable=self.timeText,
              anchor=W, width=8).grid(row=0, column=0)

        self.label_data = {}

        moles = int(self.data['num_moles'])
        if int(sqrt(moles) + 0.5) ** 2 == moles:
            columns = rows = int(sqrt(moles))
        elif moles in range(21, 30):
            columns = 5
            rows = 6
        else:
            columns = round(sqrt(moles))
            rows = round(moles / columns)
            if moles in (5, 7, 10, 13, 17, 18):
                rows += 1

        for _x in range(columns):
            for _y in range(rows):
                if len(self.label_data) < moles:
                    lbl = Label(frame2, image=self.image_list[0])
                    lbl.grid(row=_x, column=_y, padx=1, pady=1)
                    lbl.bind("<ButtonPress-1>", self.label_click)
                    _timerID = lbl.after(0, lambda: None)
                    self.label_data[lbl] = _timerID

        for _x, _y in self.label_data.items():
            sleep(.1)
            self.disappear(_x)

        self.win.update()
        self.win.minsize(self.win.winfo_width(), self.win.winfo_height())

        self.timer(None)

        sleep(.2)
        self.win.mainloop()

    def appear(self, label):
        label['image'] = self.image_list[1]
        rand = randint(self.data["min_above"], self.data["max_above"]) * 1000
        self.label_data[label] = label.after(rand, lambda: self.disappear(label))

    def disappear(self, label):
        label['image'] = self.image_list[0]
        rand = randint(self.data["min_under"], self.data["max_under"]) * 1000
        self.label_data[label] = label.after(rand, lambda: self.appear(label))

    def label_click(self, event):
        widget = event.widget
        if widget['image'] == self.image_list[1].name:
            widget['image'] = self.image_list[2]
            widget.after_cancel(self.label_data[widget])
            del self.label_data[widget]

    def timer(self, _id):
        self.timer_time = float(f'{self.timer_time - .1:.1f}')
        self.timeText.set(f'Time: {self.timer_time}')
        if self.label_data:
            if self.timer_time == 0.0:
                for _x, _y in self.label_data.items():
                    _x.after_cancel(_y)

                self.win.after_cancel(_id)
                response = messagebox.askquestion(title='Game Over', message='You ran out of time! Try again?')
                if response == 'yes':
                    self.run_again()
                if response == 'no':
                    self.win.destroy()
                    Welcome()
            else:
                new_id = self.win.after(100, lambda: self.timer(new_id))
        else:
            response = messagebox.askquestion(title='Game Over', message='Congrats! You win! Play again?')
            if response == 'yes':
                self.run_again()
            if response == 'no':
                self.win.destroy()
                Welcome()

    def run_again(self):
        self.win.destroy()
        Game(settings_dict=self.data)


if __name__ == '__main__':
    run = Welcome()
