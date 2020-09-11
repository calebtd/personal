# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Fishing Regulations
# I did not copy anyone but Mr. Blair

# Guidebook link: wildlife.utah.gov/guidebooks/2020_fishing_guidebook.pdf

# Ask where, give options
where = input("Where were you fishing? (Deer Creek, Lake Powell, Green River): ").lower
species = input("What species of fish did you catch?: ")
length = float(input("How long is the fish?: "))

if where == "deer creek":
    print(where)

if where == "lake powell":
    print(where)

if where == "green river":
    print(where)

else:
    print("Not an option. Try again.")
