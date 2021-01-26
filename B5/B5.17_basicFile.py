# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Basic File Input/Output
# I did not copy anyone

import os

# File Reading and Writing Program
print("Hi! My name is F.R.A.W.P.! I am |_redacted_| years old. My purpose is to remember things.\n"
      "The only thing I can't seem to remember is my own age...")


while True:
    name = input("\nWhat's your first and last name?: ").lower().split()
    try:
        fileName = f"{name[1]}.{name[0]}"
        if os.path.exists(fileName):
            # print("I have a file under your name!")
            existed = True
            break
        else:
            create = input("I haven't met you before. Would you like me remember you as this name? (y/n): ")
            if create == 'y':
                existed = False
                break
    except IndexError:
        print("Make sure to give a first and last name.")


with open(fileName, 'a+') as fileRW:
    fileRW.seek(0)
    file = []
    for _ in fileRW.readlines():
        x = _.replace('\n', '')
        file.append(x)

    if existed:
        if len(file) < 3:
            print(f"\nHi {name[0].capitalize()}! If my memory serves me correctly, you are\n"
                  f"{file[0]} years old and you like {file[1]} ice cream.")
            fileRW.write(input("\nWhat's your favorite place to visit?: "))
            print("Wonderful.")
        elif len(file) == 3:
            print(f"\nHi {name[0].capitalize()}! If my memory serves me correctly, you are {file[0]} years old,\n"
                  f"you like {file[1]} ice cream, and you like to visit {file[2]}.")

    else:
        age = input("Great. How old are you?: ")
        fileRW.write(f'{age}\n')
        iceCream = input("What's your favorite ice cream flavor?: ")
        fileRW.write(f'{iceCream}\n')
        print("Well, it's nice to meet you!")

print('\nHave a nice day!')
