import time

print('\rZZ', end='')
time.sleep(1)

print('\ryyy', end='')
time.sleep(1)

x = "Depositing"
for y in [".", "..", "..."]:
    print('\r{}{}'.format(x, y), end='')
    time.sleep(.5)
