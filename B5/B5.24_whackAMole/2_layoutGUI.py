# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Whack A Mole - GAME LAYOUT / GUI
# I did not copy anyone

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Label
from PIL import Image, ImageTk


def welcome_screen():
    def on_enter(lbl):
        lbl.configure(borderwidth=2)

    def on_leave(lbl):
        lbl.configure(borderwidth=1)

    x = 512
    y = 512
    welcome_win = tk.Tk()
    welcome_win.title("Whack-a-Mole")
    welcome_win['bg'] = 'black'
    welcome_win.geometry(f'{x}x{y}')
    welcome_win.minsize(x, y)
    welcome_win.maxsize(x, y)

    file = open('welcome.png', 'rb')
    welcome_image = PIL.ImageTk.PhotoImage(PIL.Image.open(file).resize((x, y - 50)))
    welcome_lbl = tk.Label(image=welcome_image)
    welcome_lbl['borderwidth'] = 0
    welcome_lbl.pack(pady=5)

    file = open('settings.png', 'rb')
    settings_image = PIL.ImageTk.PhotoImage(PIL.Image.open(file).resize((200, 25)))
    settings_lbl = tk.Label(image=settings_image)
    settings_lbl['borderwidth'] = 1
    settings_lbl.place(relx=0.3, rely=0.96, anchor=CENTER)
    settings_lbl.bind("<Button-1>", lambda arg: run_settings(True, welcome_win))
    settings_lbl.bind("<Enter>", lambda arg: on_enter(settings_lbl))
    settings_lbl.bind("<Leave>", lambda arg: on_leave(settings_lbl))

    file = open('start.png', 'rb')
    start_image = PIL.ImageTk.PhotoImage(PIL.Image.open(file).resize((130, 25)))
    start_lbl = tk.Label(image=start_image)
    start_lbl['borderwidth'] = 1
    start_lbl.place(relx=0.74, rely=0.96, anchor=CENTER)
    start_lbl.bind("<Button-1>", lambda arg: run_settings(False, welcome_win))
    start_lbl.bind("<Enter>", lambda arg: on_enter(start_lbl))
    start_lbl.bind("<Leave>", lambda arg: on_leave(start_lbl))

    welcome_win.mainloop()


def run_settings(val, window):
    global screen_bool
    if val:
        screen_bool = True
    else:
        screen_bool = False
    window.destroy()


if __name__ == '__main__':
    screen_bool = None
    welcome_screen()
