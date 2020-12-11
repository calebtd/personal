# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Defining Functions
# I did not copy anyone


# 1. None

# 2. def

# 3. The order in which they were put in, unless otherwise specified

# 4. a) Reusing the same code, therefore making your code shorter
#    b) Breaking your code into smaller, more understandable sections

# 5.
import math


def sphereArea(r):
    return 4 * math.pi * (r ** 2)


def sphereVolume(r):
    return (4 / 3) * math.pi * (r ** 3)


print('--Sphere Volume and Area--')
radius = int(input("Radius: "))
print('Sphere Volume =', sphereVolume(radius))
print('Sphere Area =', sphereArea(radius))


# 6.

def triangle_area(a, b, c):
    return (a + b + c) / 2


print('\n--Triangle Area--')
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

def optional(*args):
    return args


# 8.

def default(var=42):
    return var


# 9.

# x is global
# y, a, and b are local

# I don't know what to do with the x in y=x+3 because
# it's never defined locally or called with global.
# I would expect it was supposed to be used in the function as a global variable
