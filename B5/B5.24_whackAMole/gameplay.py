from random import randint
from time import *
from tkinter import *
from tkinter import messagebox
from math import *


# TODO
# Format moles (closest square)

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
            else:
                new_id = self.win.after(100, lambda: self.timer(new_id))
        else:
            response = messagebox.askquestion(title='Game Over', message='Congrats! You win! Play again?')
            if response == 'yes':
                self.run_again()

    def run_again(self):
        self.win.destroy()
        Game(settings_dict=self.data)


if __name__ == '__main__':
    settings = {"num_moles": 20,
                "min_under": 1,
                "max_under": 5,
                "min_above": 1,
                "max_above": 1,
                "time": 20}
    game = Game(settings_dict=settings)
