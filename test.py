# class Employee:
#     def __init__(self, wage, hours):
#         self.wage = wage
#         self.hours = hours
#
#     def calc_salary(self):
#         if self.hours > 40:
#             gross = (self.wage * 40) + ((self.hours - 40) * (self.wage * 1.5))
#         else:
#             gross = self.wage * self.hours
#
#         net = gross - (gross * .20) - (gross * .075)
#
#         return gross, net
#
#
# run = Employee(9.5, 46)
# print(run.calc_salary())

from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
print(filename)
