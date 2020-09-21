# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Captain Jack Assignment
# I did not copy anyone. This is my original work

# import math

# print backstory

print("\nYour name is Captain Jack. You are the captain of the Black Pearl.\n"
      "You and your crew have had a successful few months plundering and finding treasure,\n"
      "and you're all ready for a break. You finally pull up to the dock and see...")
input("(Press Enter to continue...)")

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

print("You address your crew and say: '...Here's three coins for each of you, \n"
      "go into town and have some fun. We'll figure out how to best divvy up our shares'")

crew = int(input("How many crew members are there? (including you and your first mate): "))
coins = int(input("How many coins are there?: "))
coins -= ((crew - 2) * 3)

# go into town
print("You and your first mate stay behind, and decide to take some extra for yourselves.\n"
      "You take 12% and you agree to give him 8%")

# coins -=

print(coins)
