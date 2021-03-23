# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Payroll for FluffShuffle Electronics
# I did not copy anyone

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *


class Employee:
    def __init__(self, number, name, address, wage, hours):
        self.number = number
        self.name = name
        self.address = address
        self.wage = wage
        self.hours = hours

    def calc_salary(self):
        if self.hours > 40:
            gross = (self.wage * 40) + ((self.hours - 40) * (self.wage * 1.5))
        else:
            gross = self.wage * self.hours

        net = gross - (gross * .20) - (gross * .075)
        return f'${net}'


def parse_employees():
    num_employees = int(len(dataList) / 4)
    for _ in range(num_employees):
        p_idx = _ * 4
        p_number = int(dataList[p_idx])
        p_name = dataList[p_idx + 1]
        p_address = dataList[p_idx + 2]
        p_wage = float(dataList[p_idx + 3].split()[0])
        p_hours = float(dataList[p_idx + 3].split()[1])
        emp = Employee(p_number, p_name, p_address, p_wage, p_hours)
        employeeList.append(emp)


def data_clear():
    global pageNum
    global dataList
    global employeeList
    pageNum = 0
    dataList = []
    employeeList = []
    text1.set('')
    text2.set('')
    text3.set('')


def page(key):
    global pageNum
    num_employees = int(len(dataList) / 4)
    if key:
        if pageNum < num_employees - 1:
            pageNum += 1
    elif not key:
        if pageNum >= 1:
            pageNum -= 1
    text1.set(employeeList[pageNum].name)
    text2.set(employeeList[pageNum].address)
    text3.set(employeeList[pageNum].calc_salary())


def open_file():
    root = Tk()
    root.withdraw()
    path = filedialog.askopenfilename()
    root.destroy()
    with open(path) as data:
        for line in data:
            dataList.append(line.strip('\n'))
    parse_employees()


dataList = []
employeeList = []
pageNum = 0

win = tk.Tk()
win.title("FluffShuffle Electronics")
win.geometry("400x300")

menuBar = Menu(win)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open", command=lambda: [data_clear(), open_file(), page(False)])
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=win.quit)
menuBar.add_cascade(label="File", menu=fileMenu)

open_file()

win.columnconfigure([0, 1], weight=1, minsize=50)
win.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1, minsize=50)

labelList = ['Name: ', 'Address: ', 'Net Pay: ']
for idx, x in enumerate(labelList):
    lbl = tk.Label(text=x)
    lbl.grid(row=idx, column=0)

text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()

page(None)

ent1 = tk.Entry(width=40, textvariable=text1)
ent1.grid(row=0, column=1, sticky=tk.W, pady=3)

ent2 = tk.Entry(width=40, textvariable=text2)
ent2.grid(row=1, column=1, sticky=tk.W, pady=3)

ent3 = tk.Entry(width=20, textvariable=text3)
ent3.grid(row=2, column=1, sticky=tk.W, pady=3)

btn = ttk.Button(win, text='Previous', command=lambda: page(False))
btn.grid(row=5, column=0, sticky=tk.E)

btn = ttk.Button(win, text='Next', command=lambda: page(True))
btn.grid(row=5, column=1, sticky=tk.W)

win.config(menu=menuBar)
win.attributes('-topmost', True)
win.update()
win.attributes('-topmost', False)
win.mainloop()
