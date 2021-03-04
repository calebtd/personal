# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Bowling Team - Feb 26

# The problem is to get data from a bowling
# game, sort it, and print it back

# I learned to take a step back and don't
# make it harder than it needs to be


# This function prints each line to the screen and saves
# the line to a list, eventually going into the file
def printout(to_print):
    global output
    output.append(f'{to_print}\n')
    print(to_print)


# Establish dictionary/list
scores = {}
output = []

# Loop to get all names and scores
while True:
    splitter = input("First name and score: ").split()

    # When it gets a blank line, break
    if not splitter:
        print()
        break
    else:
        # Turn the score into an int and add it to the dictionary
        try:
            score_int = int(splitter[-1])
            scores[splitter[0]] = score_int
        except ValueError:
            print("Make sure all scores are numbers.")

# Create a new dictionary for the asterisks
scoresAsterisk = {}

for key, value in scores.items():
    if value == 300:
        key = '*'+key  # Add asterisk
    scoresAsterisk[key] = value

# Check for longest string in the keys to format properly
longest_key = max(map(len, scoresAsterisk))

# Each of these uses the printout function
# to go to the screen AND the file

printout('--Order entered--')
for key, value in scoresAsterisk.items():
    printout(f'{key:{longest_key}} - {value}')

printout('\n--High score--')
for key in sorted(scoresAsterisk, key=scoresAsterisk.get, reverse=True):
    printout(f'{key:{longest_key}} - {scoresAsterisk[key]}')

# This one is special because it needs to sort
# without the asterisk and then add it back in
printout('\n--Alphabetical--')
for key in sorted(scores):
    if scores[key] == 300:
        newKey = '*'+key
    else:
        newKey = key
    printout(f'{newKey:{longest_key}} - {scores[key]}')

# Get the max and min scores
maxKey = max(scores, key=scores.get)
minKey = min(scores, key=scores.get)

# Display messages
printout(f"\nCongrats to {maxKey} for a high score of {scores[maxKey]}!")
printout(f"Better luck next time, {minKey}, with {scores[minKey]}.")

# Calculate average
addedScore = 0
for val in scores.values():
    addedScore += val
averageScore = addedScore // len(scores)
printout(f"The team average score is {averageScore}.")

# Write each line to the file
with open('game_results.txt', 'w') as resultsFile:
    for line in output:
        resultsFile.write(line)
