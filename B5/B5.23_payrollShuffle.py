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


def parse_employees():
    num_employees = int(len(dataList) / 4)
    for x in range(num_employees):
        idx = x * 4
        p_number = int(dataList[idx])
        p_name = dataList[idx + 1]
        p_address = dataList[idx + 2]
        p_wage = float(dataList[idx + 3].split()[0])
        p_hours = float(dataList[idx + 3].split()[1])
        emp = Employee(p_number, p_name, p_address, p_wage, p_hours)
        employeeList.append(emp)


dataList = []
employeeList = []

Tk().withdraw()
filename = askopenfilename()
# filename = 'data.txt'
with open(filename) as data:
    for line in data:
        dataList.append(line.strip('\n'))

parse_employees()
