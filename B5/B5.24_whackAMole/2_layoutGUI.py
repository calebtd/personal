# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Whack A Mole - GAME LAYOUT / GUI
# I did not copy anyone

from tkinter import *


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
            print(True)
        elif btn == 1:
            print(False)

    @staticmethod
    def on_enter(btn):
        btn.widget.config(relief='sunken')

    @staticmethod
    def on_leave(btn):
        btn.widget.config(relief='ridge')


if __name__ == '__main__':
    Welcome()
