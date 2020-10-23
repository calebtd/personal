# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Random Numbers Assignment
# I did not copy anyone

# ─────────
# PROBLEM 1
# ─────────

import math
import random
import turtle

x = 0
y = 0
t = turtle
t.speed(5000)

for loop in range(1000):

    angle = random.random() * 2 * math.pi
    x += math.cos(angle) * 2
    y += math.sin(angle) * 2

    t.goto(x, y)

dist = (x - 0) + (y - 0)
print(f"The distance between the starting point\n"
      f"and the ending point is {dist:.4f}")

# ─────────
# PROBLEM 2
# ─────────
