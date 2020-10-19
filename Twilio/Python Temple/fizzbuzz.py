import sys

order = sys.argv
order.pop(0)

for index, item in enumerate(order, start=1):
    item = int(item)
    if item % 3 == 0 and item % 5 == 0:
        print('fizzbuzz')

    elif item % 3 == 0:
        print('fizz')

    elif item % 5 == 0:
        print('buzz')

    else:
        print(item)
