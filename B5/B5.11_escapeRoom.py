# This is an escape room. The user is in a long dark hallway.
# They must figure out how to get through the locked door at the end.
# There is a table in the middle of the room with a key on it.
# The user cannot see the key unless the lights are on and they are
# standing next to the table.

# create a variable to track the position of the user. (1-5)
#   5  Door
#   4  empty
#   3  table
#   2  empty
#   1  starting point

import time


# Define function for a dot animation. Just for looks.
def dot(x):
    for y in [".", "..", "...", "...."]:
        # use \r for a carriage return, use end='' to prevent new line
        print(f"\r{x}{y}", end='')
        time.sleep(.45)


position = 1
lights = "off"
print(
    "You are in an escape room.  There is a locked door in the room.  Your task is to find a way out.  "
    "Type 'help' at any time for a list of commands.")

while True:

    # ask the user what they want to do
    command = input("What do you want to do?: ").lower()

    if command == "forward":
        if position ==
        # move the user forward one position
        position = position + 1
        print("You are now at position :", position)

    elif command == "help":
        print("Here is a list of commands:")
        print("help - list of available commands")
        print("forward - moves the user forward one position")
        print("look - tells the user what they can see")

    elif command == "look":
        dot("Looking around")

        if position == 1:
            if lights == "off":
                # tell user we can't see and give them a hint
                print(
                    "It's really dark in here.  I can't see anything.  I feel a switch on the wall. "
                    "Type 'lights on' to flip the switch.")
            else:
                # tell them what we see down the hall. (Don't tell them the key is
                # on the table unless they are standing right next to it.)
                print(
                    "I see a long hallway with a locked door at the end.  "
                    "There is a medium sized table in the middle of the hall.")

        # elif position == 2:
    elif command == "lights on":
        if lights == "on":
            print("The lights are already on.")
        else:
            # turn the lights on
            lights = "on"
            print("The lights are now on.")
    elif command == "this is lame I quit":
        break
    else:
        print("Command not recognized.")

print("game over!")
