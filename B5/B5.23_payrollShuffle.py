# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Payroll for FluffShuffle Electronics
# I did not copy anyone

from tkinter import Tk
from tkinter.filedialog import askopenfilename


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

        return gross, net


Tk().withdraw()
filename = askopenfilename()

with open(filename) as data:
    for line in data:
        print(line, end='')
