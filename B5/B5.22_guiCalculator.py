import tkinter as tk
from tkinter import messagebox
from tkinter import *

win = tk.Tk()
win['bg'] = '#202020'
win.title("Calculator")
win.geometry("302x320")

topFrame = tk.Frame(win, bg='grey')
topFrame.grid(row=1, column=0)


topText = tk.Text(topFrame, width=27, height=1)
topText.grid(row=0, column=0, padx=4, pady=1)

bottomText = tk.Text(topFrame, width=27, height=1.5)
bottomText.grid(row=1, column=0, padx=4, pady=1)

btnOne = tk.Button(topFrame, text='=', width=9, height=3, command=lambda button='=': button_click(button))
btnOne.grid(row=0, column=1, rowspan=2, padx=1, pady=1)


btnFrame = tk.Frame(win, bg="pink")
btnFrame.grid(row=2, column=0)


def button_click(key):
    print("Button pressed =>" + key)


btnOne = tk.Button(btnFrame, text='0', width=20, height=3, command=lambda button='0': button_click(button))
btnOne.grid(row=5, column=1, columnspan=2, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='1', width=9, height=3, command=lambda button='1': button_click(button))
btnOne.grid(row=4, column=1, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='2', width=9, height=3, command=lambda button='2': button_click(button))
btnOne.grid(row=4, column=2, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='3', width=9, height=3, command=lambda button='3': button_click(button))
btnOne.grid(row=4, column=3, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='4', width=9, height=3, command=lambda button='4': button_click(button))
btnOne.grid(row=3, column=1, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='5', width=9, height=3, command=lambda button='5': button_click(button))
btnOne.grid(row=3, column=2, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='6', width=9, height=3, command=lambda button='6': button_click(button))
btnOne.grid(row=3, column=3, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='7', width=9, height=3, command=lambda button='7': button_click(button))
btnOne.grid(row=2, column=1, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='8', width=9, height=3, command=lambda button='8': button_click(button))
btnOne.grid(row=2, column=2, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='9', width=9, height=3, command=lambda button='9': button_click(button))
btnOne.grid(row=2, column=3, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='.', width=9, height=3, command=lambda button='.': button_click(button))
btnOne.grid(row=5, column=3, padx=1, pady=1)

# btnOne = tk.Button(btnFrame, text='=', width=9, height=3, command=lambda button='=': button_click(button))
# btnOne.grid(row=5, column=5, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='+', width=9, height=3, command=lambda button='+': button_click(button))
btnOne.grid(row=4, column=5, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='-', width=9, height=3, command=lambda button='-': button_click(button))
btnOne.grid(row=3, column=5, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='*', width=9, height=3, command=lambda button='*': button_click(button))
btnOne.grid(row=2, column=5, padx=1, pady=1)

btnOne = tk.Button(btnFrame, text='/', width=9, height=3, command=lambda button='/': button_click(button))
btnOne.grid(row=5, column=5, padx=1, pady=1)


win.mainloop()
