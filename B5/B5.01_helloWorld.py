# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# First Program
# This is my original work, I did not copy anyone.

print('helloWorld\n')

name = input('What\'s your name?: ')

if name == 'Caleb':
    print('Welcome back, ' + name + '!')

else:
    print('Invalid User')
    quit()

print('\nI\'m missing a few things in your file. I have some \nquestions for you.')

iceCream = input("\nWhat's your favorite ice cream flavor?: ")
artist = input("Who's your favorite artist?: ")
hobby = input("What's your hobby?: ")
sport = input("What's your sport?: ")

dash = '-----------'
print('\nAlright, here\'s what I\'ve got.')
print('_______________________________')

table = {'Name': name, 'Class': 'B5', dash: dash, 'Ice Cream': iceCream, 'Artist': artist, 'Hobby': hobby,
         'Sport': sport}
for key, value in table.items():
    print(f'| {key:11}  >  {value:11} |')

print('‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾')
print("Thanks for your time!")
