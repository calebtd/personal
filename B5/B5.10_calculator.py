# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Calculator with Functions
# I did not copy anyone

class Caleb:

    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y


op = input("Operator (+,-,*,/): ")
num1 = input("First number: ")
num2 = input("Second number: ")

if op == '+':
    result = Caleb.add(num1, num2)
elif op == '-':
    result = Caleb.subtract(num1, num2)
elif op == '*':
    result = multiply(num1, num2)
elif op == '/':
    result = divide(num1, num2)

print(f"\n{num1}{op}{num2}is{result}")
