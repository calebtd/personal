# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Fishing Regulations
# I did not copy anyone but Mr. Blair

# Guidebook link: wildlife.utah.gov/guidebooks/2020_fishing_guidebook.pdf


# BUSINESS LOGIC

# Setup dictionary
rules = {
    # Setup Panguitch
    "panguitch lake": {
        # You can't keep a cutthroat or tiger trout between 15 and 22 inches
        # but everything else is fine
        "cutthroat trout": {
            "min": 14.9,
            "max": 22.1,
        },
        "tiger trout": {
            "min": 14.9,
            "max": 22.1,
        }
        # Any other fish from here you can keep.
    },
    # Setup Utah Lake
    "utah lake": {
        # All suckers HAVE to be thrown back in
        "sucker": {
            "min": 0,
            "max": 100
        }
        # Any other fish from here you can keep.
    }
}

# PROGRAM LOGIC
# Ask where, give options
where = input("Where were you fishing? (Panguitch Lake, Utah Lake): ").lower()

# If it's one of the lakes, continue. Else...line 64
if where in rules:

    species = input("What species of fish did you catch?: ").lower()

    # Only ask length IF there's info on that species
    if species in rules[where]:
        length = float(input("How long is the fish?: "))

        # Establish hierarchy and variables
        minLength = rules[where][species]["min"]
        maxLength = rules[where][species]["max"]

        # Actual logic. If the set min < the fish's length < the set max
        if minLength < length < maxLength:
            print("Sorry! You have to throw this fish out.")
            quit(0)
        # Anything else outside of min and max
        else:
            print("You can keep this fish! Do what you will with it.")
    # No specific rules for this species in this lake
    else:
        print("I don't have info on that species. You can probably keep it.")

# If it's not one of the lakes
else:
    print("I don't have that lake's database. Try a different one.")
