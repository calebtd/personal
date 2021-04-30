import tkinter as tk
from tkinter import PhotoImage
import math
import PIL.Image
import PIL.ImageTk
import random


class Game:
    def __init__(self, window, settings_dict, row, column):
        self.data = settings_dict
        self.win = window

        x = y = 256
        image0 = PhotoImage(file="sprite_0.png")
        image1 = PhotoImage(file="sprite_1.png")
        image2 = PhotoImage(file="sprite_2.png")
        self.image_list = [image0, image1, image2]
        self.timerID = None

        self.lbl = tk.Label(self.win)
        self.lbl.grid(row=row, column=column)

    def run(self):
        self.lbl['image'] = self.image_list[0]
        self.lbl.bind("<ButtonPress-1>", self.label_click)
        random_under = random.randint(0, self.data["max_under"])
        self.timerID = self.lbl.after(random_under, self.disappear)

    def appear(self):
        # swap out the image of labelOne
        print('Event Triggered')
        self.lbl['image'] = self.image_list[1]
        self.timerID = self.lbl.after(1000, self.disappear)

    def disappear(self):
        self.lbl['image'] = self.image_list[0]
        self.timerID = self.lbl.after(2000, self.appear)

    def label_click(self, event):
        print(event)
        widget = event.widget
        if widget['image'] == self.image_list[1].name:
            self.lbl['image'] = self.image_list[2]
            self.lbl.after_cancel(self.timerID)


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Whack-a-Mole")
    win.geometry('512x512')
    win.minsize(512, 512)
    settings = {"num_moles": 9,
                "min_under": 1,
                "max_under": 5,
                "min_above": 1,
                "max_above": 3,
                "time": 30}
    moleList = []
    for x in range(2):
        moleList.append(Game(win, settings, x, x))
    for x in moleList:
        x.run()
    win.mainloop()

    print('done')
