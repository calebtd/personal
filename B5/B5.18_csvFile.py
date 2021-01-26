# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Working with CSV Files
# I did not copy anyone

import csv
with open('station2.csv', 'r') as file:
    for row in csv.reader(file):
        if row[7] != '':
            print(row[7])
