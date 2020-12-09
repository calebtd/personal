# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# UVU Project: Farmer John's Field
# Due 12/3/20
# I did not copy anyone

# The problem:
#   Draw the field with turtle graphics and calculate the unwatered area

# Steps:
#   Get input with nice exceptions, draw the square, draw the circles,
#   calculate the area, print the results

# What I learned:
#   How to use try blocks better
#   How to better implement functions and solve basic math neatly


import turtle
import math


def move(h, v):
    # Function for moving the turtle easier
    t.pu()
    t.goto(h, v)
    t.pd()


def circles(a, b, r):
    # Function for drawing the circles, calls move() and then draws
    t.begin_fill()
    move(a, b)
    t.circle(r)
    t.end_fill()


# Try block for invalid input
while True:
    try:
        # Get the input
        side = int(input('Choose a size for the rectangle: '))
        # raise the exception manually if negative
        if side > 0:
            break
        else:
            raise ValueError
    # do this if there's an exception
    except ValueError:
        print("Please type a valid number code.\n")

# These variables make things easier to deal with
t = turtle.Turtle()
radius = side/2

# Make the square (with colors!)
move((side/2), (side/2))
t.color('#4F4E4F')
t.fillcolor('#4F4E4F')
t.begin_fill()
for _ in range(4):
    t.right(90)
    t.forward(side)
t.end_fill()

# Set colors back for the circles
t.color('#000000')
t.fillcolor('#FFFFFF')

# First circle
circles(-(side/2), 0, radius)

# Second circle
circles((side/2), 0, radius)

# Third circle
circles(-(side/2), -side, radius)

# Fourth circle
circles((side/2), -side, radius)

# Redraw square on top
t.color('#4F4E4F')
move((side/2), (side/2))
for _ in range(4):
    t.right(90)
    t.forward(side)
# done with turtle, so hide it
t.hideturtle()

# ---Area Logic---
# area of a square: b * h
# area of a circle quadrant: πr² / 4

# You can get the area of the unwatered section by
# subtracting 4 quadrants from the square

squareArea = side * side
quadrantArea = (math.pi * (radius**2)) / 4
unwateredArea = squareArea - (quadrantArea * 4)

# OR simplified down

notWatered = side**2 - (math.pi * (radius**2))

# print the result, rounded to 2 decimal places
print(f'The unwatered area is: {notWatered:.2f}')

turtle.done()
