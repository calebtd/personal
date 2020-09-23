# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Captain Jack Assignment
# I did not copy anyone. This is my original work


# print backstory
print("\nYour name is Captain Jack. You are the captain of the Black Pearl.\n"
      "You and your crew have had a successful few months plundering and finding treasure,\n"
      "and you're all ready for a break. You finally pull up to the dock and see...")
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
      "Gibbs and me 'ill decide 'ow best to divvy up our shares'\n")

# Ask how many crew and coins, assign to variables
crew = int(input("How many crew members are there? (including you and your first mate): "))
coins = int(input("How many coins are there?: "))

# Pull out 3 coins for each crew member, except Jack and Gibbs
coins -= ((crew - 2) * 3)

# sneaky sneaky
print("\nYou and your first mate stay behind, both wanting a bit of extra gold. \n"
      "You sneak in and take 12%, without Gibbs knowing. Then when you are \n"
      "counting it up, you agree to give Gibbs 8% for being a good first mate.")

coins //= (25/22)  # 12%
captainJack = coins

coins *= .92  # 8%
gibbs = coins

print("\nYour crew returns, and you then divide the remaining gold to everyone, \n"
      "including Gibbs and yourself.")


print(coins // crew)
print(coins % crew)
