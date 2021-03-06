# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# UVU Exercises #2
# I did not copy anyone but Mr. Blair

import math

# --------------------

# 1. List in your own words the six steps in the software development process

# restate in English
# create model
# pseudocode
# program
# test/debug
# repeat until satisfied

# --------------------

# 2. Calculate and print out the squares of the integers 1 to 5

# x = 1
# while x != 5:
#     print(x**2)
#     x = x+1
# print(x**2)

# Found an easier way
for x in range(1, 6):
    print(x ** 2)

# --------------------

# 3. Code that will print a value for pi

pi = 22 / 7
print(pi)
print(math.pi)

# --------------------

# 4. Why is it a good idea to first write out an algorithm
# in pseudocode before jumping immediately into Python code?

# You can think through all the steps and problems before they come up in code,
# so you can catch them easier. If you document the pseudocode enough, you could
# just hand that to anyone and they could program it just as well as you can.
# If you rewrite the problems into English and then into the in between of
# pseudocode, it's easier to actually implement into code.

# --------------------

# 5. Change the program to convert Fahrenheit to Celsius instead

# celsius = float(input("What is the Celsius temperature? "))
# fahrenheit = 9/5 * celsius + 32
# print("The temperature {1} is {0:,.2f} degrees Fahrenheit.".format(fahrenheit, celsius))

fahrenheit = float(input("What is the Fahrenheit temperature?: "))
celsius = (fahrenheit - 32) * 5 / 9
print("The temperature {0:,.2f} is {1:,f} degrees Celsius.".format(fahrenheit, celsius))
