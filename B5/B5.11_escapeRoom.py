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
def dot(x, t):
    print(x, end='')
    for uni in range(t):
        print('.', end='')
        time.sleep(.40)
    print('\n')


def forward():
    # move the user forward one position
    global position
    position += 1
    print("You are now at position", position)


# def tempCommands(*val):
#     if val[1] in helpDict:
#         dot(f'{val[1]}ing', 4)
#         print(val[2])
#         val[3]
#     else:
#         print("Command not recognized.")


# initial variables
position = 1
lights = doorCode = doorKey = move = haveKey = in1 = in2 = in3 = in4 = canHandle = canCode = unlocked = False

# This is the initial dictionary for the help command. This is how the user knows what to do,
# and it builds on it and deletes from it as the program goes along.
helpDict = {'Look': 'Looks around the current room',
            'Forward': 'Moves you forward one position',
            'Backward': 'Moves you backward one position',
            'Position': 'Checks your current position'}

# Nice formatting for the initial message
lines = '─' * 82
print(f'┌{lines}┐')
print("Welcome to my escape room, --The-House-of-Pythons--. Your task is to find a way out.\n"
      "Type 'help' at any time for a list of commands. (You'll need this.)")
print(f'└{lines}┘')

# Repeat this until break
while True:

    # ask the user what they want to do
    command = input("\nWhat would you like to do?: ").lower()

    # Set some variables to see if they've been in that room before
    if position == 1:
        in1 = True
    elif position == 2:
        in2 = True
        # Clear this if they've gotten to room 2
        if "Open" in helpDict:
            helpDict.pop('Open')
    elif position == 3:
        in3 = True
    elif position == 4:
        in4 = True
    elif position == 5:
        move = False
        helpDict = {'Look': 'Looks around the current room',
                    'Position': 'Checks your current position'}

    if canHandle:
        if position == 4:
            helpDict['Try Handle'] = 'Turn the handle on the door in room 4.'
        else:
            if 'Try Handle' in helpDict:
                helpDict.pop('Try Handle')

    if canCode:
        if position == 4 and not doorCode:
            helpDict['Type Code'] = 'Type to the keypad on the door in room 4'
        else:
            if 'Type Code' in helpDict:
                helpDict.pop('Type Code')

    # locations = list()
    # locations[0] = True
    # locations[1] = False
    # locations.append(True)
    # print(locations)

    # Forward command
    if command == "forward":
        if not move:
            print("You can't go forward")

        elif position == 2:
            if lights:
                forward()
            else:
                print("It's too dark, I might trip on something.")

        elif position == 4:
            if unlocked:
                forward()
            else:
                print("You can't go forward")

        else:
            forward()

    # Backward command
    elif command == "backward":
        if position == 1:
            print("You can't go backward")
        elif not move:
            print("You can't go backward")
        else:
            # move the user backward one position
            position -= 1
            print("You are now at position", position)

    # Help command. Print the dictionary in a nice looking table
    elif command == "help":
        for key, value in helpDict.items():
            print(f'{key:10}  -  {value}')

    elif command == 'position':
        print(f"You are at position {position}.")

    # Look command. Lots of logic here, it sets up what 'look' does in each room
    elif command == "look":
        dot("Looking around", 3)

        if position == 1:
            if not in2:
                print("You are in a window lit room with nothing but an unlocked door. "
                      "This must be the front entrance.")
                # add opening the front door.
                helpDict["Open"] = "Open the unlocked door you just found."
            else:
                print("Nothing new here.")

        elif position == 2:
            if not lights:
                # tell user we can't see and give them a hint
                print("It's really dark in here.  I can't see anything.")
                # add feeling the room
                helpDict["Feel"] = "Feels around the room"
            # show this only if they've been in 4 and they have the key
            elif in4 and haveKey:
                if not doorKey:
                    print("I must've missed this before. There's a tiny keyhole in the corner.")
                    helpDict['Insert Key'] = "Put the key in the keyhole you just found"
                else:
                    print("Nothing else to see here.")
            # if they've ben to 4 but don't have the key
            elif in4 and not doorKey:
                print("I must've missed this before. There's a tiny keyhole in the corner. I wonder why...")
            else:
                # tell them what we see down the hall.
                print("I see a long hallway with a locked door at the end.")

        elif position == 3:
            # do this if they haven't picked up the key yet
            if not haveKey:
                print("There's table with a key sitting on it.")
                # add pick up.
                helpDict['Pick Up'] = "Pick up the key you just found"
            # this way they can't pick in up over and over
            else:
                print("I don't see anything else in here.")

        elif position == 4:
            print("There's a locked door right in front of you. It has a keypad and a handle.")
            if haveKey:
                print("How do I unlock this thing...?")
            canHandle = True

        elif position == 5:
            print("You see a sign that says:\n"
                  "Congratulations!! You escaped! I'm impressed to say the least. Thanks for playing!")
            break

        # this ain't possible
        else:
            print("Where am I...?")

    elif command == 'feel':
        if 'Feel' in helpDict:
            dot('Feeling', 6)
            if position == 2:
                if not lights:
                    print("Oh! There's a switch!")
                    helpDict['Flip'] = "Flips the switch you found"
                else:
                    print("I don't feel anything else unusual.")
            elif position == 3:
                if in4:
                    print("There was a paper hidden under the table. It has the code 29704 on it.\n"
                          "Wasn't there a keypad somewhere?")
                    canCode = True
                else:
                    print("Nothing new here.")
            elif position == 4:
                print("Hidden in a corner you find a paper that blends in with the wall.\n"
                      "It's all folded up and kind of looks like a hint.")
                helpDict['Read Hint'] = "Read the hint you found in room 4."
            else:
                print("Nothing to feel here.")

        else:
            print("Command not recognized.")

    elif command == 'open':
        if 'Open' in helpDict:
            dot('Opening', 3)
            print("Now you can move forward.")
            move = True
            helpDict.pop('Open')
        else:
            print("Command not recognized.")

    elif command == 'flip':
        if 'Flip' in helpDict:
            lights = True
            print("Ah! There's some light.")
            helpDict.pop('Flip')
        else:
            print("Command not recognized.")

    elif command == 'pick up':
        if 'Pick Up' in helpDict:
            if position == 3:
                print("\nYou are now holding a key. Where's the keyhole?")
                haveKey = True
                helpDict.pop('Pick Up')
            else:
                print("Nothing to pick up here.")
        else:
            print("Command not recognized.")

    elif command == 'insert key':
        if 'Insert Key' in helpDict:
            if position == 2 and haveKey:
                print("\nYou put the key in the keyhole and turn it. You feel a low rumble and faint scratching.\n"
                      "It must've unlocked something in a different room.")
                haveKey = False
                doorKey = True
                helpDict.pop('Insert Key')
            else:
                print("Nowhere to insert here.")
        else:
            print("Command not recognized.")

    elif command == 'try handle':
        if 'Try Handle' in helpDict:
            if position == 4:
                if not doorKey and not doorCode:
                    print("Nothing budges.")
                elif doorKey and not doorCode:
                    print("The door moves as if the deadbolt is unlocked, but I still can't turn the handle.")
                elif not doorKey and doorCode:
                    print("The handle turns, but I still can't open the door.")
                elif doorCode and doorKey:
                    print("It opened! You can now go forward.")
                    canHandle = False
                    unlocked = True
            else:
                print("You can't do that here.")
        else:
            print("Command not recognized.")

    elif command == 'type code':
        if 'Type Code' in helpDict:
            inputCode = int(input('Type code: '))
            if inputCode == 29704:
                print("Code Accepted")
                doorCode = True
                canCode = False
                helpDict.pop('Type Code')
            else:
                print("Incorrect.")
        else:
            print("Command not recognized.")

    elif command == 'read hint':
        if 'Read Hint' in helpDict:
            print("You unfold the paper and find a bunch a garbled words...\n\n"
                  "     !tey epacse yam uoy    \n"
                  "     ,pu ti peek uoy fI  \n"
                  "     .teb tseb ruoy eb yam     \n"
                  "     gnileeF dna gnikooL      ")
        else:
            print("Command not recognized.")

    # elif command == "quit":
    #     break

    elif command == "idk":
        print("try typing help")
    elif command == 'explode':
        print("You have exploded.")
        break

    # elif command == 'debug':
    #     lights = doorFront = move = in4 = doorKey = canHandle = True
    #     helpDict["Feel"] = "Feels around the room"

    else:
        print("Command not recognized.")


print("\nGame Over!")
