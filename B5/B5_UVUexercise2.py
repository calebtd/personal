# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# UVU Exercises #2
# I did not copy anyone but Mr. Blair

import math

# 1. List in your own words the six steps in the software development process

# restate in English
# create model
# pseudocode
# program
# test/debug
# repeat until satisfied

# 2. Calculate and print out the squares of the integers 1 to 5
x = 1
while x != 5:
    print(x**2)
    x = x+1
print(x**2)


# 3. Code that will print a value for pi
pi = 22/7
print(pi)
print(math.pi)


# 4. Why is it a good idea to first write out an algorithm
# in pseudocode before jumping immediately into Python code?


# 5. Change the program to convert Fahrenheit to Celsius instead

# celsius = float(input("What is the Celsius temperature? "))
# fahrenheit = 9/5 * celsius + 32
# print("The temperature {1} is {0:,.2f} degrees Fahrenheit.".format(fahrenheit, celsius))

fahrenheit = float(input("What is the Fahrenheit temperature? "))
celsius = (fahrenheit - 32) * 5/9
print("The temperature {0:,.2f} is {1} degrees Celsius.".format(fahrenheit, celsius))
