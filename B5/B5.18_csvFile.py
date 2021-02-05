# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Working with CSV Files
# I did not copy anyone

import csv

# Problem 1
with open('stations-filtered.csv', 'w', newline='') as filteredFile:
    writer = csv.writer(filteredFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('station2.csv', 'r') as stationFile:
        for row in csv.reader(stationFile):
            if row[7] != '':
                writer.writerow(row)

# Problem 2
drainage = []
with open('stations-filtered.csv', 'r', newline='') as filteredFile:
    reader = csv.reader(filteredFile)
    next(reader)
    for row in reader:
        drainage.append(float(row[7]))

with open('drainage-area-avg.txt', 'w') as drainageAverage:
    x = 0
    y = len(drainage)
    for value in drainage:
        x += value
    result = x / y
    drainageAverage.write(str(result))
    # print(f'{result:.4f}')

# Problem 3

# ord('')
# chr()

# fileName = input("What's the input file name?: ")
# shift = input("How many shift values?: ")

fileName = 'text.txt'
shift = 5

with open(f'{fileName}.txt') as cleanFile:
    for word in cleanFile:
        for letter in word:
            pass
