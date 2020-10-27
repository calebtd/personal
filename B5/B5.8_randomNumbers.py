# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Random Numbers Assignment - 10/23/20
# I did not copy anyone

# ─────────
# PROBLEM 1
# ─────────

import math
import random
import turtle

# ask for number of steps, positive int only
steps = int(input('How many steps would you like the random walk to take?: '))
while steps < 1:
    print("Please input a positive number.")
    steps = int(input('How many steps would you like the random walk to take?: '))

# setup variables
x = 0
y = 0
t = turtle
t.speed(5000)

# provided walk code
for n in range(steps):
    angle = random.random() * 2 * math.pi
    x += math.cos(angle) * 2
    y += math.sin(angle) * 2

    t.goto(x, y)

# go back to beginning, draws a line as well
t.goto(0, 0)

# print actual distance traveled
print(f"\nThe actual distance traveled was {steps} steps")
# print distance formula between first and last position
dist = math.sqrt(((x - 0)**2) + ((y - 0)**2))
print(f"The distance between the starting point "
      f"and the ending point was {dist:.4f}")

# pause for next section, clear turtle
input("\nPress Enter...")
t.clear()

# ─────────
# PROBLEM 2
# ─────────
# define function to make moving easier


def move(q, w):
    t.pu()
    t.goto(q, w)
    t.pd()


# setup variables
t = turtle
t.width(1)
t.speed(11)

# Apple system colors
colors = ('#0a84ff', '#30d158', '#5e5ce6',
          '#ff9f0a', '#ff375f', '#bf5af2',
          '#ff453a', '#64d2ff', '#ffd60a')

# Discord system colors
bgcolors = ('#7289DA', '#FFFFFF', '#99AAB5',
            '#2C2F33', '#23272A', '#000000')

# forever loop
while True:

    # do this 5 times
    for i in range(5):
        # pick a random color for turtle
        t.color(random.choice(colors))

        # set random heading
        t.seth(random.randint(1, 360))

        # draw a circle with random parameters
        radius = random.randint(5, 150)
        extent = random.randint(1, 360)
        steps = random.randint(1, 100)

        t.circle(radius, extent, steps)

        # move back to 0 and start over
        move(0, 0)

    # after repeating that 5 times, change background
    # no one wants a seizure
    t.bgcolor(random.choice(bgcolors))
