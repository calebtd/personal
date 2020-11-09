# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Calculator with Functions
# I did not copy anyone

# This escape room has just a few more things than what's required.
# I have the same basic layout, but with some added puzzles. Player must find the key,
# the code, where to put them in, and do things in the right order.

# Spoilers!
# 5 - Ending Room
# 4 - With with final door
# 3 - Room with table for Key and Code
# 2 - Room with lightswitch and keyhole
# 1 - Starting room with first door.

# Define function for a dot animation. Just for looks.
import time


def dot(x, t):  # x is the text to put in, t is how many dots
    print(x, end='')
    for uni in range(t):
        print('.', end='')
        time.sleep(.40)
    print('\n')


# A function for moving the player forward
def forward():
    global position
    position += 1
    print("You are now at position", position)


# Same thing, but backward
def backward():
    global position
    position -= 1
    print("You are now at position", position)


# initial variables
position = 1
lights = doorCode = doorKey = move = haveKey = unlocked \
    = in1 = in2 = in3 = in4 = canHandle = canCode = False

# This is the initial dictionary for the help command. This is how the user knows what to do,
# and it builds on it and deletes from it as the program goes along. It also tells the program
# whether or not it can run commands.
helpDict = {'Forward': 'Moves you forward one position',
            'Backward': 'Moves you backward one position',
            'Position': 'Checks your current position',
            '----------': '',
            'Look': 'Looks around the current room'}

# Nice formatting for the initial message
lines = '─' * 82
print(f'┌{lines}┐')
print("Welcome to my escape room, --The-House-of-Pythons--. Your task is to find a way out.\n"
      "Type 'help' at any time for a list of commands.  (This is essential, as it changes.)")
print(f'└{lines}┘')

# Repeat this until break
while True:
    # Inside here has a few sections. First there's the setups, things to do before actually
    # running stuff the users see. Second, the commands the user can always do. This includes
    # Look, Forward, Backward, Position, and Help. Third, the commands that are added to the
    # dictionary as the game goes on. After that, there's just a print game over outside of the loop.

    # ask the user what they want to do
    command = input("\nWhat would you like to do?: ").lower()

    # SECTION 1 #

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
        # When they get here, they've won, so take out the normal stuff
        move = False
        helpDict = {'Look': 'Looks around the current room',
                    'Position': 'Checks your current position'}

    # If they can turn the handle at this point...
    if canHandle:
        # and if they're in room 4, put that command in. Else...
        if position == 4:
            helpDict['Try Handle'] = 'Turn the handle on the door in room 4.'
            print('**New Command**.')
        # pull it out
        else:
            if 'Try Handle' in helpDict:
                helpDict.pop('Try Handle')

    # Same thing as the above section, but for typing in the code.
    if canCode:
        if position == 4 and not doorCode:
            helpDict['Type Code'] = 'Type to the keypad on the door in room 4'
            print('**New Command**.')
        else:
            if 'Type Code' in helpDict:
                helpDict.pop('Type Code')

    # SECTION 2 #

    # Forward command
    if command == "forward":
        if not move:
            if position == 1:
                print("You can't go forward. Try typing help.")
            else:
                print("You can't go forward.")
        # if the lights aren't on, don't continue
        elif position == 2:
            if lights:
                forward()
            else:
                print("It's too dark, I might trip on something.")
        # don't go forward in room 4 unless the game is done
        elif position == 4:
            if unlocked:
                forward()
            else:
                print("You can't go forward.")
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
            backward()

    # Help command. Print the dictionary in a nice looking table
    elif command == "help":
        for key, value in helpDict.items():
            print(f'{key:10}  -  {value}')

    # check position
    elif command == 'position':
        print(f"You are at position {position}.")

    # Look command. Lots of logic here, it sets up what 'look' does in each room
    elif command == "look":
        # aesthetics
        dot("Looking around", 3)

        if position == 1:
            # if they haven't been to 2 yet
            if not in2:
                print("You are in a window lit room with nothing but an unlocked door. "
                      "This must be the front entrance.")
                # add opening the front door.
                helpDict["Open"] = "Open the unlocked door you just found."
                print('**New Command**.')
            else:
                print("Nothing new here.")

        elif position == 2:
            if not lights:
                # tell user we can't see and give them a hint
                print("It's really dark in here.  I can't see anything.")
                # add feeling the room
                helpDict["Feel"] = "Feels around the room"
                print('**New Command**.')
            # show this only if they've been in 4 and they have the key
            elif in4 and haveKey:
                if not doorKey:
                    print("I must've missed this before. There's a tiny keyhole in the corner.")
                    # add putting the key in
                    helpDict['Insert Key'] = "Put the key in the keyhole you just found"
                    print('**New Command**.')
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
            if not haveKey and not doorKey:
                print("There's table with a key sitting on it.")
                # add pick up.
                helpDict['Pick Up'] = "Pick up the key you just found"
                print('**New Command**.')
            # this way they can't pick it up over and over
            else:
                print("I don't see anything else in here.")

        elif position == 4:
            print("There's a locked door right in front of you. It has a keypad and a handle.")
            if haveKey:
                # point out that a lack of key commands is not a bug
                print("How do I unlock this thing...?")
            # They can try turning the handle if they're in room 4
            canHandle = True

        elif position == 5:
            # this is the end. THIS IS HOW TO FINISH
            print("You see a sign that says:\n"
                  "Congratulations!! You escaped! I'm impressed to say the least. Thanks for playing!")
            break

        # this ain't possible
        else:
            print("Where am I...?")

    # SECTION 3 #

    # Just like look, lots of logic.
    elif command == 'feel':
        if 'Feel' in helpDict:
            dot('Feeling', 4)

            if position == 2:
                if not lights:
                    # This is how to turn on the lights
                    print("Oh! There's a switch!")
                    helpDict['Flip'] = "Flips the switch you found"
                    print('**New Command**.')
                else:
                    print("I don't feel anything else unusual.")
            elif position == 3:
                # Once they've been to 4 before, they can do this
                if in4:
                    print("There was a paper hidden under the table. It has the code 29704 on it.\n"
                          "Wasn't there a keypad somewhere?")
                    canCode = True
                else:
                    print("Nothing new here.")
            elif position == 4:
                # This is how to get the hint.
                if 'Read Hint' in helpDict:
                    print('Nothing new here.')
                else:
                    print("Hidden in a corner you find a paper that blends in with the wall.\n"
                          "It's all folded up and kind of looks like a hint.")
                    # add read hint
                    helpDict['Read Hint'] = "Read the hint you found in room 4."
                    print('**New Command**.')
            else:
                print("Nothing to feel here.")
        else:
            print("Command not recognized.")

    # only applicable to the very beginning with the first door.
    elif command == 'open':
        if 'Open' in helpDict:
            dot('Opening', 3)
            print("Now you can move forward.")
            move = True
            helpDict.pop('Open')
        else:
            print("Command not recognized.")

    # this is flipping on the light switch
    elif command == 'flip':
        if 'Flip' in helpDict:
            lights = True
            print("Ah! There's some light.")
            helpDict.pop('Flip')
        else:
            print("Command not recognized.")

    # This is picking up the key
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

    # This is for putting the key in the keyhole at room 2
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

    # This is for turning the handle in room 4. It has a few different outcomes,
    # depending on things being unlocked. If all is unlocked, it opens and then
    # you can move forward and beat the game.
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

    # This is for typing the code into the door in 4.
    # You can only type it in if you've seen the code in 3
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

    # This is for reading the hint you can find in 4. It can be read anywhere,
    # it just adds into the dictionary. The text is reversed both ways.
    elif command == 'read hint':
        if 'Read Hint' in helpDict:
            print("You unfold the paper and find a bunch a garbled words...\n\n"
                  "     !tey epacse yam uoy    \n"
                  "     ,pu ti peek uoy fI  \n"
                  "     .teb tseb ruoy eb yam     \n"
                  "     gnileeF dna gnikooL      ")
        else:
            print("Command not recognized.")

    # easter egg from my brother
    elif command == 'explode':
        print("You have exploded.")
        break

    elif command == 'debug':
        lights = doorFront = move = in4 = canHandle = True
        helpDict["Feel"] = "Feels around the room"

    else:
        print("Command not recognized.")


print("\nGame Over!")
