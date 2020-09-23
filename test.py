coins = 1000
crew = 20
PBA = 0

coins -= 18 * 3
print(coins)

jack = coins // (25/3)
coins //= 25/22
PBA += coins % (25/22)

gibbs = coins // (25/2)
coins //= (25/23)
PBA += coins % (25/23)

PBA += coins % crew
split = coins // crew

print(jack)
print(gibbs)
print(split)
print(PBA)
