import sys

arg_1 = int(sys.argv[1])
arg_2 = int(sys.argv[2])
arg_sum = arg_1 + arg_2

if arg_sum <= 0:
    print('You have chosen the path of destitution.')

elif 1 <= arg_sum <= 100:
    print('You have chosen the path of plenty.')

elif arg_sum > 100:
    print('You have chosen the path of excess.')
