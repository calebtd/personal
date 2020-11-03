# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Calculator with Functions
# I did not copy anyone


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


result = 0

while True:

    num1 = int(input("\nFirst number: "))
    op = input("Operator (+,-,*,/): ")
    num2 = int(input("Second number: "))

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)

    print(f"\n{num1} {op} {num2} is {result}")
