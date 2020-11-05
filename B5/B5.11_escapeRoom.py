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
        time.sleep(.45)
    print('\n')


# def tempCommands(*val):
#     if val[1] in helpDict:
#         dot(f'{val[1]}ing', 4)
#         print(val[2])
#         val[3]
#     else:
#         print("Command not recognized.")


# initial variables
position = 1
lights = doorFront = doorCode = doorKey = move = haveKey = in1 = in2 = in3 = in4 = False

helpDict = {'Look': 'Looks around the current room',
            'Forward': 'Moves you forward one position',
            'Backward': 'Moves you backward one position'}

lines = '─' * 82
print(f'┌{lines}┐')
print("Welcome to my escape room, --The-House-of-Pythons--. Your task is to find a way out.\n"
      "Type 'help' at any time for a list of commands.")
print(f'└{lines}┘')

while True:

    # ask the user what they want to do
    command = input("\nWhat would you like to do?: ").lower()

    if position == 1:
        in1 = True
    elif position == 2:
        in2 = True
        if "Open" in helpDict:
            helpDict.pop('Open')
    elif position == 3:
        in3 = True
    elif position == 4:
        in4 = True
    elif position == 5:
        move = False

    if command == "forward":
        if not doorFront and position == 4:
            print("You can't go forward")
        elif not move:
            print("You can't go forward")
        else:
            # move the user forward one position
            position += 1
            print("You are now at position", position)

    elif command == "backward":
        if position == 1:
            print("You can't go backward")
        else:
            # move the user backward one position
            position -= 1
            print("You are now at position", position)

    elif command == "help":
        for key, value in helpDict.items():
            print(f'{key:9}  -  {value}')

    elif command == "look":
        dot("Looking around", 4)

        if position == 1:
            if not in2:
                print("You are in a window lit room with nothing but an unlocked door. "
                      "This must be the front entrance.")
                helpDict["Open"] = "Open the unlocked door you just found."
            else:
                print("Nothing new here.")

        elif position == 2:
            if not lights:
                # tell user we can't see and give them a hint
                print("It's really dark in here.  I can't see anything.")
                helpDict["Feel"] = "Feels around the room"
            elif in4 and haveKey:
                print("I must've missed this before. There's a tiny keyhole in the corner.")
                helpDict['Insert Key'] = "Put the key in the keyhole you just found"
            elif in4:
                print("I must've missed this before. There's a tiny keyhole in the corner. I wonder why...")
            else:
                # tell them what we see down the hall. (Don't tell them the key is
                # on the table unless they are standing right next to it.)
                print("I see a long hallway with a locked door at the end.")

        elif position == 3:
            if not haveKey:
                print("There's table with a key sitting on it.")
                helpDict['Pick Up'] = "Pick up the key you just found"
            else:
                print("I don't see anything else in here.")

        elif position == 4:
            print("There's a locked door right in front of you. It has a keypad and a handle.\n"
                  "How do I unlock this thing...?")

        elif position == 5:
            print("You see a sign that says:\n"
                  "Congratulations!! You escaped! I'm impressed to say the least. Thanks for playing!")
            break

        # this ain't possible
        else:
            print("Where am I...?")

    elif command == 'open':
        if 'Open' in helpDict:
            dot('Opening', 3)
            print("Now you can move forward.")
            move = True
            helpDict.pop('Open')
        else:
            print("Command not recognized.")

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
            if position == 2:
                print("\nYou put the key in the keyhole and turn it. You feel a low rumble and faint scratching.\n"
                      "It must've unlocked something in a different room.")
                haveKey = False
                doorKey = True
                helpDict.pop('Insert Key')
                helpDict['Try Handle'] = 'Turn the handle on the door in room 4.'
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
                    print("The door moves as if the deadbolt is unlocked, but I still can't move the handle.")
                elif not doorKey and doorCode:
                    print("The handle turns, but I still can't open the door.")
                else:
            else:
                print("You can't do that here.")
        else:
            print("Command not recognized.")

    # elif command == 'type code'

    elif command == 'hint':
        if 'Hint' in helpDict:
            pass
        else:
            print("Command not recognized.")

    elif command == "quit":
        break

    else:
        print("Command not recognized.")


print("Game Over!")
