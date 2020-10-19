import sys

order = sys.argv
order.pop(0)

for index, item in enumerate(order, start=1):
    print(f"{index}. {item}")
