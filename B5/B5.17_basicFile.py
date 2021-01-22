# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Basic File Input/Output
# I did not copy anyone

import os

# print("Hi! My name is FORUM. My age is irrelevant, don't you think?\n"
#       "My purpose is to remember things. ")

while True:
    name = input("\nWhat's your first and last name?: ").lower().split()
    try:
        fileName = f"{name[1]}.{name[0]}"
        if os.path.exists(fileName):
            print("I have a file under your name!")
            break
        else:
            create = input("I haven't met you before. Would you like me to create a file for you? (y/n): ")
            if create == 'y':
                open(fileName, 'x')
                break
    except IndexError:
        print("Make sure to give a first and last name.")

fileRead = open(fileName)
fileWrite = open(fileName, 'w')

print(fileRead.readlines())

fileRead.close()
fileWrite.close()
