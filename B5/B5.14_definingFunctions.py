# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Defining Functions
# I did not copy anyone

# 1.

# 2.

# 3.

# 4.

# 5.

# 6.
def triangle_area(a, b, c):
    return (a + b + c)/2


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
