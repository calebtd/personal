# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Defining Functions
# I did not copy anyone

import turtle
import math


def move(t, h, v):
    t.pu()
    t.goto(h, v)
    t.pd()


a = b = c = d = turtle.Turtle()
x = y = 0
r = 10

# A
move(a, x, y)
a.circle()
