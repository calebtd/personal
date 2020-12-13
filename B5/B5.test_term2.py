# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Term 2 Test Part 2 (Program)
# I did not copy anyone

# --- Part 1 ---

def get_smallest(a, b):
    if a <= b:
        return a
    elif a >= b:
        return b


while True:
    try:
        num1 = int(input('Value for first number: '))
        num2 = int(input('Value for second number: '))
        break
    except ValueError:
        print('Invalid input.\n')

print('\nThe smaller number is:', get_smallest(num1, num2))

# --- Part 2 ---

n = r = a = b = y2 = y1 = x2 = x1 = 1

import math

(3+4) * 5

(n * (n - 1)) / 2

4 * math.pi * (r ** 2)

math.sqrt((r * (math.cos(a) ** 2)) + (r * (math.cos(b) ** 2)))

(y2 - y1) / (x2 - x1)
