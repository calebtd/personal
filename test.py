coins = 1000
crew = 20
PBA = 0

coins -= (crew - 2) * 3

jack = int(coins * .12)
coins -= jack

gibbs = int(coins * .08)
coins -= gibbs

split = coins // crew
coins -= split * crew

jack += split
gibbs += split

print(jack)
print(gibbs)
print(split)
print(coins)

print("\n┌─────────────────────┐")
table = {'Jack': jack,
         'Gibbs': gibbs,
         'Crew': split,
         'PBA': coins}
for key, value in table.items():
    print(f'│ {key:6}  -  {value:8} │')
print("└─────────────────────┘")

