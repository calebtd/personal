from random import randint
from time import *
from tkinter import *
from tkinter import messagebox


# TODO
# Format moles (closest square)


def appear(label):
    label['image'] = image_list[1]
    rand = randint(1, 1) * 1000
    label_data[label] = label.after(rand, lambda: disappear(label))


def disappear(label):
    label['image'] = image_list[0]
    rand = randint(1, 5) * 1000
    label_data[label] = label.after(rand, lambda: appear(label))


def label_click(event):
    widget = event.widget
    if widget['image'] == image_list[1].name:
        widget['image'] = image_list[2]
        widget.after_cancel(label_data[widget])
        del label_data[widget]


def timer(_id):
    global timer_time
    timer_time = float(f'{timer_time - .1:.1f}')
    timeText.set(timer_time)

    print(timer_time)
    if label_data:
        if timer_time == 0.0:
            for _x, _y in label_data.items():
                _x.after_cancel(_y)
            win.after_cancel(_id)
            again = messagebox.askquestion(title='Game Over', message='You ran out of time! Try again?')
            win.destroy()
            if again:
                pass

        else:
            new_id = win.after(100, lambda: timer(new_id))
    else:
        messagebox.showinfo(title='Game Over', message='Congrats! You win!')


win = Tk()
win.title('whack test')

frame1 = Frame(win)
frame2 = Frame(win, background='#D3D3D3', padx=1, pady=1)
frame1.pack()
frame2.pack(padx=10, pady=10)

timeText = StringVar()

lbl1 = Label(frame1, text='Time:', font=('Agency FB', 40)).grid(row=0, column=0)
lbl2 = Label(frame1, font=('Agency FB', 40), textvariable=timeText, width=5, anchor=W).grid(row=0, column=1)

image0 = PhotoImage(file="sprite_0.png")
image1 = PhotoImage(file="sprite_1.png")
image2 = PhotoImage(file="sprite_2.png")
image_list = [image0, image1, image2]

label_data = {}

# ------------------------------------

for x in range(3):
    for y in range(4):
        lbl = Label(frame2, image=image_list[0])
        lbl.grid(row=x, column=y, padx=1, pady=1)
        lbl.bind("<ButtonPress-1>", label_click)
        timerID = lbl.after(0, lambda: None)
        label_data[lbl] = timerID

for x, y in label_data.items():
    sleep(.1)
    disappear(x)

win.update()
win.minsize(win.winfo_width(), win.winfo_height())

timer_time = 5
timeText.set(timer_time)

timer(None)

sleep(.2)
win.mainloop()
