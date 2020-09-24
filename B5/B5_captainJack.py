# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Captain Jack Assignment
# I did not copy anyone. This is my original work


# Start with id
print("\nYour name is Captain Jack. You are the captain of the Black Pearl.\n"
      "You and your crew have had a successful few months plundering and \n"
      "finding treasure, and you're all ready for a break.\n")

# Ask how many crew and coins, assign to variables
crew = int(input("How many crew members do you have? (including you and your first mate): "))
coins = int(input("How many coins did you get?: "))

# Print backstory
print("\nYou and your crew finally pull up to the dock and see:")

# wait instead of displaying everything at once
input("(Press Enter to continue...)")

# ASCII Art just for fun
print(""
      " __          __  _                             _        \n"
      " \ \        / / | |                           | |       \n"
      "  \ \  /\  / /__| | ___ ___  _ __ ___   ___   | |_ ___  \n"
      "   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \  | __/ _ \ \n"
      "    \  /\  /  __/ | (_| (_) | | | | | |  __/  | || (_) |\n"
      "     \/  \/_\___|_|\___\___/|_| |_| |_|\___|   \__\___/ \n"
      "         |__   __|       | |                            \n"
      "   "
      "         | | ___  _ __| |_ _   _  __ _  __ _         \n"
      "            | |/ _ \| '__| __| | | |/ _` |/ _` |        \n"
      "            | | (_) | |  | |_| |_| | (_| | (_| |        \n"
      "            |_|\___/|_|   \__|\__,_|\__, |\__,_|        \n"
      "                                     __/ |              \n"
      "                                    |___/")

# Tell crew what to do
print("You address your crew and say: 'A good season we've 'ad, ey?\n"
      "Plenty a' gold for all of us. Now who's up for some fun in \n"
      "Tortuga! 'Ere's three coins for each o' you, and shove off. \n"
      "Gibbs and me 'ill decide 'ow best to divvy up our shares.'")

# wait instead of displaying everything at once
input("(Press Enter)")

# Pull out 3 coins for each crew member, except Jack and Gibbs
coins -= (crew - 2) * 3

# sneaky sneaky
print("\nYou and your first mate stay behind, both wanting a bit of extra gold.\n"
      "You sneak in and take 12%, without Gibbs knowing. Later, when you and Gibbs\n"
      "are counting the coins up, you decide to give Gibbs 8% for being a good first mate.")

# wait instead of displaying everything at once
input("(Press Enter)")

# pull 12% for Jack
jack = int(coins * .12)  # int so there's no decimals
coins -= jack  # shortcut for coins - jack

# pull for Gibbs, same as Jack but 8%
gibbs = int(coins * .08)
coins -= gibbs

# divide evenly
print("\nYour crew returns, so you then divide the remaining gold to everyone, \n"
      "including Gibbs and yourself.\n"
      "Any remaining coins go to the Pirate's Benevolent Association.")

# use // for just int division
split = coins // crew
# anything after goes to PBA
coins -= split * crew

# split to Jack and Gibbs too
jack += split
gibbs += split

print("\nHere's how many gold coins everyone gets:")

# wait instead of displaying everything at once
input("(Press Enter)")

# print a nice looking table
print("\n┌─────────────────────┐")
table = {'Jack': jack,
         'Gibbs': gibbs,
         'Crew': split,
         'PBA': coins}
for key, value in table.items():
    print(f'│ {key:6}  -  {value:8} │')
print("└─────────────────────┘")
