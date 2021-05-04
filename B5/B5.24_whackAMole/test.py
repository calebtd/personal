import random
import time
import tkinter as tk
from tkinter import PhotoImage

# TODO
# Add timer
# Format window
# Format moles (closest square)


def appear(label):
    label['image'] = image_list[1]
    rand = random.randint(1, 1) * 1000
    label_data[label] = label.after(rand, lambda: disappear(label))


def disappear(label):
    label['image'] = image_list[0]
    rand = random.randint(1, 5) * 1000
    label_data[label] = label.after(rand, lambda: appear(label))


def label_click(event):
    widget = event.widget
    if widget['image'] == image_list[1].name:
        widget['image'] = image_list[2]
        widget.after_cancel(label_data[widget])


win = tk.Tk()
win.title('whack test')
win.geometry('512x512')
win.minsize(512, 512)

image0 = PhotoImage(file="sprite_0.png")
image1 = PhotoImage(file="sprite_1.png")
image2 = PhotoImage(file="sprite_2.png")
image_list = [image0, image1, image2]

label_data = {}

# ------------------------------------

for x in range(3):
    for y in range(3):
        lbl = tk.Label(win, image=image_list[0])
        lbl.grid(row=x, column=y)
        lbl.bind("<ButtonPress-1>", label_click)
        timerID = lbl.after(0, lambda: None)
        label_data[lbl] = timerID

for x, y in label_data.items():
    time.sleep(.1)
    disappear(x)

time.sleep(.2)
win.mainloop()
