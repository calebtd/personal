# Caleb Dillenbeck
# B5 Programming
# Demo of IF statements
# I did not copy anyone or anything but Mr. Blair :D

import shutil

# steve is lucky
name = input("What's your name?: ").lower()

if name == "steve":
    print("Congrats! You just won a free movie pass!")

yearInSchool = input("\nWhat year in school are you?: ").lower()

if yearInSchool == "freshmen":
    excited = input("\nAre you excited for high school? (yes, no): ").lower()

    if excited == "yes":
        lp = input("Good! Are you going to Lone Peak? (yes, no): ")
        if lp == "yes":
            print("Good. You can now be my friend.")
        else:
            print("You are no longer my friend. JK lol.")


elif yearInSchool == "sophomore":
    ready = input("\nAre you ready to drive? (yes, no): ").lower()
    if ready == "yes":
        print("Good! You're more prepared than I was!")

elif yearInSchool == "junior":
    readyACT = input("Nice! Are you ready for the ACT? (yes, no): ").lower()
    if readyACT == "yes":
        print("Hey that's awesome! Good on you.")
    else:
        print("That's something you should probably get on.")

elif yearInSchool == "senior":
    readyGrad = input("You ready to graduate? (yes, no): ").lower()
    if readyGrad == "yes":
        print("That's exciting! Good luck on whatever comes next!")
    else:
        print("Yeah. Me neither.")

elif yearInSchool == "super senior":
    print("Alright Mr. Blair. Time to move on. XD")


columns = shutil.get_terminal_size().columns
print("\n\n\n\n")
print("G a m e   O v e r".center(columns))
