import time
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

        image0 = PhotoImage(file="sprite_0.png")
        image1 = PhotoImage(file="sprite_1.png")
        image2 = PhotoImage(file="sprite_2.png")
        self.image_list = [image0, image1, image2]
        self.timerID = None

        self.lbl = tk.Label(self.win)
        self.lbl.grid(row=row, column=column)
        self.lbl.bind("<ButtonPress-1>", self.label_click)

    def run(self):
        self.lbl['image'] = self.image_list[0]
        self.disappear()

    def appear(self):
        # swap out the image of labelOne
        # print('Event Triggered')
        self.lbl['image'] = self.image_list[1]
        rand = random.randint(self.data["min_under"], self.data["max_under"]) * 1000
        print(rand)
        self.timerID = self.lbl.after(rand, self.disappear)

    def disappear(self):
        self.lbl['image'] = self.image_list[0]
        rand = random.randint(self.data["min_above"], self.data["max_above"]) * 1000
        self.timerID = self.lbl.after(rand, self.appear)

    def label_click(self, event):
        print(event)
        widget = event.widget
        if widget['image'] == self.image_list[1].name:
            self.lbl['image'] = self.image_list[2]
            self.lbl.after_cancel(self.timerID)
            return True


if __name__ == '__main__':
    win = tk.Tk()
    win.title("Whack-a-Mole")
    win.geometry('512x512')
    win.minsize(512, 512)
    settings = {"num_moles": 9,
                "min_under": 1,
                "max_under": 5,
                "min_above": 1,
                "max_above": 1,
                "time": 30}
    moleList = []

    for x in range(3):
        for y in range(3):
            moleList.append(Game(win, settings, x, y))
    print(moleList)
    for x in moleList:
        x.run()
        time.sleep(.1)
    win.mainloop()

    print('done')
