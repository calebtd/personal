# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Defining Functions
# I did not copy anyone

import math


# 1. None

# 2. def

# 3. The order in which they were put in, unless otherwise specified

# 4. a) Reusing the same code, therefore making your code shorter
#    b) Breaking your code into smaller, more understandable sections

# 5.
def sphereArea(r):
    return 4 * math.pi * r ** 2


def sphereVolume(r):
    return (4 / 3) * math.pi * r ** 3


radius = int(input("Radius: "))
print('Sphere Volume =', sphereVolume(radius))
print('Sphere Area =', sphereArea(radius))


# 6.
def triangle_area(a, b, c):
    return (a + b + c) / 2


while True:
    try:
        x = int(input('First side length: '))
        y = int(input('Second side length: '))
        z = int(input('Third side length: '))
        break
    except ValueError:
        print("Please type valid numbers.\n")

print(triangle_area(x, y, z))

# 7.

# 8.
