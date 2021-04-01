# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Payroll for FluffShuffle Electronics
# Due April 16
# I did not copy anyone

# This program will read a company's employee data from a file and display it in a Tkinter GUI.
# It needs to use list, vars, and/or classes to organize data.

# First, it has the Employee class, that gets the data and calculates salary.
# It has lots of functions for the different steps, including: picking/opening
# the file, parsing file data into variables and classes, changing pages on the
# GUI, and clearing the data when a new file is opened. It then sets up the
# window and uses the data from the functions to fill it in.

# Import needed libraries
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from tkinter import *


# Define the employee class. Brings in the info on init,
# calculates the salary in the function.
class Employee:
    """Takes all the variable needed to create and employee object"""
    def __init__(self, number, name, address, wage, hours):
        self.number = number
        self.name = name
        self.address = address
        self.wage = wage
        self.hours = hours

    def calc_salary(self):
        """Takes the employee's wage and hours to calculate
        pay after overtime and deductions. Returns net pay as a string"""
        # If overtime, normal wage plus time and a half on remaining hours
        if self.hours > 40:
            gross = (self.wage * 40) + ((self.hours - 40) * (self.wage * 1.5))
        else:
            gross = self.wage * self.hours

        # Deductions
        net = gross - (gross * .20) - (gross * .075)

        # Return in USD format with 2 decimals
        return f'${net:,.2f}'


def parse_employees(p_datalist):
    """Takes a list with the file's content, sorts it into individual
    variables, and creates objects with those vars. No returns"""
    # Employee info comes in blocks of 4. Divide the whole thing
    # by four to figure out how many employees are in the file
    num_employees = int(len(p_datalist) / 4)
    for _ in range(num_employees):
        # This index will go to the next employee on each iteration
        p_idx = _ * 4
        p_number = int(p_datalist[p_idx])
        p_name = p_datalist[p_idx + 1]
        p_address = p_datalist[p_idx + 2]
        p_wage = float(p_datalist[p_idx + 3].split()[0])
        p_hours = float(p_datalist[p_idx + 3].split()[1])

        # Make the objects, and stick em' in a list
        emp = Employee(p_number, p_name, p_address, p_wage, p_hours)
        employeeList.append(emp)


def data_clear():
    """Clears out the variables and lists when opening a new file"""
    global pageNum
    global dataList
    global employeeList
    pageNum = 0
    dataList = []
    employeeList = []
    text1.set('')
    text2.set('')
    text3.set('')


# Show the correct info on the correct UI page
def page(key):
    """Takes True or False to move forward or backward a page in the GUI.
    It sets the text in each of the entry boxes. No returns"""
    global pageNum
    num_employees = int(len(dataList) / 4)
    # Don't go below the first page or above the max amount of pages
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
    """Opens the file dialogue and inserts each line into a list.
    Calls the parse_employees function with the list when done"""
    root = Tk()
    root.withdraw()  # Don't open another window, only the file picker
    path = filedialog.askopenfilename()
    root.destroy()
    # Open the file picked, insert each line into the list
    with open(path) as data:
        for line in data:
            dataList.append(line.strip('\n'))

    parse_employees(dataList)


# Start of the program
# Make needed vars/lists
dataList = []
employeeList = []
pageNum = 0

# Let's get crackin'! Open the file, start parsing data
open_file()

# Define the Tkinter window
win = tk.Tk()
win.title("FluffShuffle Electronics")
win.geometry("400x300")
win.minsize(350, 175)

# These make the window resizeable
win.columnconfigure([0, 1], weight=1, minsize=50)
win.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7], weight=1, minsize=50)

# Make the 'File' Menu with: open a new file, and exit the program
menuBar = Menu(win)
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Open", command=lambda: [data_clear(), open_file(), page(None)])
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=win.quit)
menuBar.add_cascade(label="File", menu=fileMenu)


# Make the labels in front of the entry boxes
labelList = ['Name: ', 'Address: ', 'Net Pay: ']
for idx, x in enumerate(labelList):
    lbl = tk.Label(text=x)
    lbl.grid(row=idx, column=0)

# This enables changing the text in the entry boxes
text1 = tk.StringVar()
text2 = tk.StringVar()
text3 = tk.StringVar()

# Place the entry boxes
ent1 = tk.Entry(width=40, textvariable=text1)
ent1.grid(row=0, column=1, sticky=tk.W, pady=3)

ent2 = tk.Entry(width=40, textvariable=text2)
ent2.grid(row=1, column=1, sticky=tk.W, pady=3)

ent3 = tk.Entry(width=20, textvariable=text3)
ent3.grid(row=2, column=1, sticky=tk.W, pady=3)

# Make and place the buttons to switch pages
btn = ttk.Button(win, text='Previous', command=lambda: page(False))
btn.place(relx=0.35, rely=0.9, anchor=CENTER)

btn = ttk.Button(win, text='Next', command=lambda: page(True))
btn.place(relx=0.65, rely=0.9, anchor=CENTER)


# Go to the first page
page(None)

# Start the GUI
win.config(menu=menuBar)

# These bring the window to the front, then disables staying at front
win.attributes('-topmost', True)
win.update()
win.attributes('-topmost', False)

win.mainloop()
