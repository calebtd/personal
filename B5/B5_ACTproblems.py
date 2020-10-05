# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Common ACT Math Problems Assignment
# I did not copy anyone but Mr. Blair

# I did the Quadratic Formula, Area of a Triangle, and Circumference of a Circle problems

import math

# Tell user the purpose of each section

# QUADRATIC
print("\nThis will calculate the x-intercepts of a quadratic equation.")
print("The equation is x = −b ± √b²-4ac/2a")

# Ask input for each number
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

# Calculate using the quadratic formula with plus
x = (-b + math.sqrt(b**2 - (4 * a * c))) / 2 * a
# Then with minus
y = (-b - math.sqrt(b**2 - (4 * a * c))) / 2 * a

# Print the results
print("X = {} or {}".format(x, y))

####################

# AREA OF TRIANGLE
print("\nThis will calculate the area of a triangle.")
print("The equation is (1/2) (base) (height)")

# Ask for the base and for the height
b = float(input("Base: "))
h = float(input("Height: "))

# Solve
a = .5 * b * h

# Print results
print("The area is {}".format(a))

####################

# CIRCUMFERENCE
print("\nThis will calculate the circumference of a circle from the radius")
print("The equation is circumference = 2π * r")

# Ask for radius
r = float(input("Radius: "))

# Solve
c = 2 * math.pi * r

# Print results
print("The circumference is {:0.2f}".format(c))
