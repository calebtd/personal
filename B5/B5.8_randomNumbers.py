# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Common ACT Math Problems Assignment
# I did not copy anyone

import math
import random
import turtle

x = 0
y = 0
t = turtle
t.speed(5000)

while True:

    angle = random.random() * 2 * math.pi
    x += math.cos(angle) * 2
    y += math.sin(angle) * 2

    t.goto(x, y)
