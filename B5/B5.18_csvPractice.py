# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# CSV Practice
# I did not copy anyone

import csv


def printer(index):
    table = {
        'Ride name': index[2],
        'Park': index[0],
        'Section': index[1],
        'Height': index[3],
        'Categories': index[4],
        'Hours': index[5]}
    print('\n')
    for key, value in table.items():
        print(f'{key:10}  -  {value:1}')


search = input('Enter search term: ')

with open('DisneyWorldAttractions.csv', newline='\n') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
    next(csvReader)

    count = 0
    for row in csvReader:
        if search.lower() in row[2].lower():
            count += 1
            printer(row)
