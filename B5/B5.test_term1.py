# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Test Part 2 (Program)
# I did not copy anyone

total = 0

# welcome
print("\nWelcome to Arches National Park! I'm glad you could make it today.        \n"
      "There is a fee for park entrance so let's get that taken care of, shall we? \n"
      "Here's a table with all the info you need...")

# print table
print('\n', "-"*50, "\n",
      "| Mode of transport | Base Fee | Occupants Fee          \n",
      "-"*50, "\n",
      "| Private Vehicle   | $12.00   | $1 per person ($8 Max) \n",
      "| Motorcycle        | $8.00    | N/A                    \n",
      "| Bicycle           | $3.00    | N/A                    \n",
      "| Walking           | N/A      | $1.50 per person       \n",
      "-"*50)

# ask what mode of transport
trans = input("\nWhat mode of transportation?: ").lower()

# ask how many people inside of the if blocks
# calculate cost and display as currency
if trans == "private vehicle":
    # only ask if applicable
    people = int(input("How many people?: "))

    # if between 1 and 8 people, base fee plus people
    # CHAINED VS SIMPLIFIED
    if people >= 1 and people <= 8:
        total = 12 + people

    # if over 8, just straight 20
    elif people >= 8:
        total = 20

    # anything else is wrong
    else:
        print("Invalid Input")
        quit()

# easy clap. motorcycle 8
elif trans == "motorcycle":
    total = 8

# even easier. bicycle 3
elif trans == "bicycle":
    total = 3

# walking has no base, just the amount of people
elif trans == "walking":
    # only ask if applicable
    people = int(input("How many people?: "))

    # if it's 1 or higher, 1.5 * people
    if people >= 1:
        total = (1.5 * people)

    # anything else is wrong
    else:
        print("Invalid Input")
        quit()

# anything else is wrong
else:
    print("Invalid Input")
    quit()

# print out the total baybee
print("Your total is ${0:,.2f}".format(total))
