# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Bowling Team
# I did not copy anyone


# Function for printing lists nicely
def print_table(dictionary, sorter=False):  # Pass the dictionary, pass a sorter if there is one
    # Newline
    print()
    # Get the length of the longest dictionary key, use that to space the printed list
    longest_key = max(map(len, dictionary))

    # Format the list if there's an asterisk
    for values in dictionary.values():
        if values == 300:
            longest_key += 1

    if not sorter:
        for keys, values in dictionary.items():
            if values == 300:
                keys = f'*{keys}'
            print(f'{keys:{longest_key}} - {values}')
    else:
        pass

    print()
    for w in sorted(dictionary, key=dictionary.get, reverse=True):
        print(f'{w:{longest_key}} - {dictionary[w]}')

    print()
    for w in sorted(dictionary):
        print(w, dictionary[w])


# Establish dictionary
scores = {}

# Loop to get all names and scores
while True:
    splitter = input("Name and score: ").split()

    # When it gets a blank line, break
    if not splitter:
        break
    else:
        # Check for a perfect game
        # if splitter[-1] == '300':
        #     splitter[0] = f'*{splitter[0]}'

        # Turn the score into an int
        try:
            score_int = int(splitter[-1])
            scores[splitter[0]] = score_int
        except ValueError:
            print("Make sure all scores are numbers.")

# Print in input order
print_table(scores)


# Print in numerical order
# print_table(scores, 1)  # The 1 is for the lambda, sort by the value index

# Print in alphabetical order
# print_table(scores, 0)  # The 0 is for the lambda, sort by the key index


# Get the key for max and min values
maxKey = max(scores, key=scores.get)
minKey = min(scores, key=scores.get)

print(f"\nCongrats to {maxKey} for a high score of {scores[maxKey]}!")
print(f"Better luck next time {minKey}, with {scores[minKey]}.")

addedScore = 0
for val in scores.values():
    addedScore += val
averageScore = addedScore // len(scores)
print(f"The team average score is {averageScore}.")

with open('game_results.txt', 'w') as resultsFile:
    pass
