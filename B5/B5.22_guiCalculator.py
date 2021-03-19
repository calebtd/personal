import tkinter as tk
from tkinter import messagebox
from tkinter import *

win = tk.Tk()
win['bg'] = '#202020'
win.title("Calculator")
win.geometry("302x290")


def buttonClick(button):
    print("Button pressed =>" + button)


btnZero = tk.Button(win, text='0', width=20, height=3, command=lambda button='0': buttonClick(button))
btnZero.grid(row=5, column=1, columnspan=2, padx=1, pady=1)

btnOne = tk.Button(win, text='1', width=9, height=3, command=lambda button='1': buttonClick(button))
btnOne.grid(row=4, column=1, padx=1, pady=1)

btnTwo = tk.Button(win, text='2', width=9, height=3, command=lambda button='2': buttonClick(button))
btnTwo.grid(row=4, column=2, padx=1, pady=1)

btnThree = tk.Button(win, text='3', width=9, height=3, command=lambda button='3': buttonClick(button))
btnThree.grid(row=4, column=3, padx=1, pady=1)

btnFour = tk.Button(win, text='4', width=9, height=3, command=lambda button='4': buttonClick(button))
btnFour.grid(row=3, column=1, padx=1, pady=1)

btnFive = tk.Button(win, text='5', width=9, height=3, command=lambda button='5': buttonClick(button))
btnFive.grid(row=3, column=2, padx=1, pady=1)

btnSix = tk.Button(win, text='6', width=9, height=3, command=lambda button='6': buttonClick(button))
btnSix.grid(row=3, column=3, padx=1, pady=1)

btnSeven = tk.Button(win, text='7', width=9, height=3, command=lambda button='7': buttonClick(button))
btnSeven.grid(row=2, column=1, padx=1, pady=1)

btnEight = tk.Button(win, text='8', width=9, height=3, command=lambda button='8': buttonClick(button))
btnEight.grid(row=2, column=2, padx=1, pady=1)

btnNine = tk.Button(win, text='9', width=9, height=3, command=lambda button='9': buttonClick(button))
btnNine.grid(row=2, column=3, padx=1, pady=1)

btnPoint = tk.Button(win, text='.', width=9, height=3, command=lambda button='.': buttonClick(button))
btnPoint.grid(row=5, column=3, padx=1, pady=1)

btnEquals = tk.Button(win, text='=', width=9, height=3, command=lambda button='=': buttonClick(button))
btnEquals.grid(row=5, column=5, padx=1, pady=1)

btnPlus = tk.Button(win, text='+', width=9, height=3, command=lambda button='+': buttonClick(button))
btnPlus.grid(row=4, column=5, padx=1, pady=1)

btnMinus = tk.Button(win, text='-', width=9, height=3, command=lambda button='-': buttonClick(button))
btnMinus.grid(row=3, column=5, padx=1, pady=1)

btnTimes = tk.Button(win, text='*', width=9, height=3, command=lambda button='*': buttonClick(button))
btnTimes.grid(row=2, column=5, padx=1, pady=1)

btnDivide = tk.Button(win, text='/', width=9, height=3, command=lambda button='/': buttonClick(button))
btnDivide.grid(row=0, column=5, rowspan=2, padx=1, pady=1)

topText = tk.Text(win, width=27, height=1)
topText.grid(row=0, column=1, columnspan=3, padx=1, pady=1)

bottomText = tk.Text(win, width=27, height=1.5)
bottomText.grid(row=1, column=1, columnspan=3, padx=1, pady=1)


win.mainloop()
