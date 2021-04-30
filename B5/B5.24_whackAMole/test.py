import tkinter as tk
from tkinter import PhotoImage

win = tk.Tk()
win.title('whack test')
win.geometry('300x300')

noSnakeImg = PhotoImage(file="sprite_0.png")
snakeImg = PhotoImage(file="sprite_1.png")
snakeAttackImg = PhotoImage(file="sprite_2.png")


def display_snake():
    # swap out the image of labelOne
    print('Event Triggered')
    lblOne['image'] = snakeImg
    lblOne.after(1000, display_no_snake)


def display_no_snake():
    lblOne['image'] = noSnakeImg
    lblOne.after(2000, display_snake)


lblOne = tk.Label(win, image=noSnakeImg)
lblOne.grid(row=0, column=0)

display_snake()


win.mainloop()
