# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# GUI Calculator
# I did not copy anyone

import tkinter as tk
from tkinter import *


# Function for calc buttons and text boxes
def button_click(key):
    print("Button pressed -> " + key)
    global clear
    if key == '=':
        try:
            bottomText.delete(1.0, END)
            txt_input = topText.get(1.0, END)
            bottomText.insert(tk.END, eval(txt_input))
            clear = True
        except SyntaxError:
            bottomText.insert(tk.END, 'Syntax Error')
            print('Syntax Error')
        except ZeroDivisionError:
            bottomText.insert(tk.END, 'Zero Division')
            print('Zero Division')
    elif key == '+/-':
        topText.insert(1.0, '-')
    elif key == 'C':
        topText.delete(1.0, END)
        bottomText.delete(1.0, END)
    elif key == '⌫':
        topText.delete('end -2 chars', END)
    else:
        if clear:
            topText.delete(1.0, END)
            clear = False
        topText.insert(tk.END, key)


# Initials. Set variable, color, size, and title
win = tk.Tk()
win['bg'] = '#202020'
win.title("Calculator")
win.geometry("302x350")
clear = False  # Used later for the function

# Set Frames. Sticky sticks it to the windows border. It halfway worked
btnFrame = tk.Frame(win, bg="pink")
btnFrame.grid(row=2, column=0, sticky=N + S + E + W)


# Text boxes. One for input, one for results
topText = tk.Text(win, width=36, height=1)
topText.grid(row=0, column=0, padx=4, pady=1)

bottomText = tk.Text(win, width=36, height=1.5)
bottomText.grid(row=1, column=0, padx=4, pady=1)


# These variables are used in the following
# loops to name the buttons
zero = ('+/-', 'C', '⌫', '/')
one = ('7', '8', '9', '*')
two = ('4', '5', '6', '-')
three = ('1', '2', '3', '+')

order = (zero, one, two, three)

for num, y in enumerate(order):
    for idx, x in enumerate(y):
        btn = tk.Button(btnFrame, text=x, width=9, height=3, command=lambda button=x: button_click(button))
        btn.grid(row=num, column=idx, padx=1, pady=1)


# Other buttons that don't fit in
btn = tk.Button(btnFrame, text='0', width=20, height=3, command=lambda button='0': button_click(button))
btn.grid(row=5, column=0, columnspan=2, padx=1, pady=1)

btn = tk.Button(btnFrame, text='.', width=9, height=3, command=lambda button='.': button_click(button))
btn.grid(row=5, column=2, padx=1, pady=1)

btn = tk.Button(btnFrame, text='=', width=9, height=3, command=lambda button='=': button_click(button))
btn.grid(row=5, column=3, padx=1, pady=1)

# Run
win.mainloop()
