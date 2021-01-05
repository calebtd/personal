# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Lists and List Operations Exercise
# I did not copy anyone

import random

# 1
print('Problem 1:')

disneyCharacters = ['Mickey', 'Donald', 'Goofy', 'Minnie']

print(disneyCharacters[0], disneyCharacters[1])
print(disneyCharacters[1], disneyCharacters[0])
print(disneyCharacters[1], disneyCharacters[2])
print(disneyCharacters[3], disneyCharacters[2], disneyCharacters[1], disneyCharacters[0])

# 2
print('\nProblem 2:')

s1 = [2, 1, 4, 3]
s2 = ['c', 'a', 'b']

print(s1 + s2)          # [2, 1, 4, 3, c, a, b]
print(3 * s1 + 2 * s2)  # [2, 1, 4, 3, 2, 1, 4, 3, 2, 1, 4, 3, c, a, b, c, a, b]
print(s1[1])            # 1
print(s1[1:3])          # 1, 4, 3
print(s1 + s2[-1])      # 2, 1, 4, 3, b

# 3
print('\nProblem 3:')


def shuffle(myList):
    new_list = []
    for x in myList:
        new_list.pop(myList[random.randint(0, len(myList))])
    return new_list


line = ['Bob', 'Gretchen', 'Jane', 'Jim']
print(shuffle(line))
