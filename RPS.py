# Caleb Dillenbeck
import random

wins = 0
losses = 0
print(
    'Welcome to rock paper scissors. For now, it\'s just random, \nbut I may add an algorithm later. Type "d" when '
    'done.\n')
print('Rock(R), Paper(P), Scissors(S)')
move_list = ['R', 'P', 'S']

while True:
    usr = input('\nYour move: ').upper()
    cpu = random.choice(move_list)

    # Clean up so the user can type any variation
    if usr == 'ROCK':
        usr = 'R'
    if usr == 'PAPER':
        usr = 'P'
    if usr == 'SCISSORS':
        usr = 'S'

    if usr == cpu:
        print('CPU: ' + cpu + '')
        print('It\'s a tie!')

    elif usr == 'R':
        print('CPU: ' + cpu + '')
        if cpu == 'P':
            print('You lose.')
            losses += 1
        else:
            print('You win!')
            wins += 1

    elif usr == 'P':
        print('CPU: ' + cpu + '')
        if cpu == 'S':
            print('You lose.')
            losses += 1
        else:
            print('You win!')
            wins += 1

    elif usr == 'S':
        print('CPU: ' + cpu + '')
        if cpu == 'R':
            print('You lose.')
            losses += 1
        else:
            print('You win!')
            wins += 1

    elif usr == 'D':
        print('G a m e   O v e r')
        print('Wins: ', wins)
        print('Losses: ', losses)
        break

    # easter egg
    # elif usr == '':

    else:
        print('Invalid input, try again.')
