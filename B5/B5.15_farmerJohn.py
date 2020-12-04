# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Farmer John
# I did not copy anyone

import turtle
import math


def move(t, h, v):
    t.pu()
    t.goto(h, v)
    t.pd()


a = b = c = d = turtle.Turtle()
# b = turtle.Turtle()
# c = turtle.Turtle()
# d = turtle.Turtle()

s = turtle.Turtle()

x = y = 0
r = 50
dist = 50

while True:
    try:
        rect = int(input('Choose a size for the rectangle'))
        break
    except ValueError:
        print("Please type a valid number code.\n")

# S
move(s, -50, 100)
s.color('#D3D3D3')
s.fillcolor('#D3D3D3')
s.begin_fill()
for _ in range(4):
    s.forward(rect)
    s.right(90)
s.end_fill()


# A
move(a, x-dist, y+dist)
a.fillcolor('#FFFFFF')
a.begin_fill()
a.circle(r)
a.end_fill()

# B
move(b, x+dist, y+dist)
a.begin_fill()
b.circle(r)
a.end_fill()

# C
move(c, x-dist, y-dist)
a.begin_fill()
c.circle(r)
a.end_fill()

# D
move(d, x+dist, y-dist)
a.begin_fill()
d.circle(r)
a.end_fill()


turtle.exitonclick()
