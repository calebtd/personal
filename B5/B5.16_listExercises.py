# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Lists and List Operations Exercise
# I did not copy anyone

import random

# 1
print('Problem 1')

disneyCharacters = ['Mickey', 'Donald', 'Goofy', 'Minnie']

print(disneyCharacters[0:2:])
print(disneyCharacters[-3:-5:-1])
print(disneyCharacters[1:3:])
print(disneyCharacters[-1:-5:-1])

# 2
print('\nProblem 2')

# A. [2, 1, 4, 3, c, a, b]
# B. [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, 'c', 'a', 'b', 'c', 'a', 'b']
# C. 1
# D. [1, 4]
# E. TypeError
print("Check Comments.")

# 3
print('\nProblem 3')


def shuffle(mylist):
    new_list = []
    length = len(mylist)
    for _ in range(length):
        randint = random.randint(0, len(mylist) - 1)
        new_list.append(mylist.pop(randint))
    return new_list


line = ['Bob', 'Gretchen', 'Jane', 'Jim']
print(shuffle(line))

# 4
print('\nProblem 4')


def innerProd(x, y):
    length = len(x)
    new_list = []
    for _ in range(length):
        new_list.append(x[_] * y[_])
    return new_list


list_X = [1, 2, 3]
list_Y = [3, 2, 1]
print(innerProd(list_X, list_Y))

# 5
print('\nProblem 5')


def getLongestName(mylist):
    mylist.sort(key=len)
    return mylist[-1]


favNames = []
name_input = input("Tell me your favorite names (enter 'd' when done): ")
favNames.append(name_input)
while True:
    name_input = input("Next: ")
    if name_input == 'd':
        if len(favNames) < 2:
            print("Please add at least 2 items.")
        else:
            break
    else:
        favNames.append(name_input)

print("\nThe longest name is ->", getLongestName(favNames))

# 6
print('\nProblem 6')

vowels = ['a', 'e', 'i', 'o', 'u']
vowel_count = 0
name = input("What's your name?: ").lower()
for char in name:
    if char in vowels:
        vowel_count += 1
print(f"Your name has {vowel_count} vowel(s) in it.")

# Extra credit
print("\nExtra Credit Problem")

# put string to check here
paragraph = '''
President Trump has been asking aides and lawyers, including White House counsel Pat Cipollone, about his 
self-pardon power, multiple sources tell CNN. 

Some of those conversations have happened in recent weeks, one of the sources said. It is unclear if it has 
come up since the mayhem at the Capitol building yesterday fomented by the President’s rhetoric or after his 
recent controversial call with the Georgia secretary of state. Trump has asked about the legal and political 
consequences of a self-pardon, according to a source close to the President. He has also asked for legal 
opinions on whether he has the authority to issue a self-pardon and has been advised on the potential political 
fallout. This person said it was not yet clear whether the President would follow through with a pardon for himself.
'''.lower()

# put the word you want to check for here
word = "the"

wordcount = 0
for char in paragraph.split():
    if char == word:
        wordcount += 1
print(f'''The word "{word}" is used {wordcount} times.''')

# End
print("\n\nThank you! Bye!!")
