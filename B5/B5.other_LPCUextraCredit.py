# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Lone Peak Credit Union
# I did not copy anyone but Mr. Blair

# This program simulates an ATM at the newly created Lone Peak Credit Union
# The application supports making deposits and withdrawals from the account
# There is only one account and one user. No password required

import time
import mysql_cursor

# start connection
conn = mysql_cursor.Connection('home.dillenbeck.org', 'caleb', '/.ssh/id_rsa',
                               'caleb', '/sql_pass.txt', 'caleb')


# set up function for moving progress dots. functions are fun!!
def dot(x):
    for y in [".", "..", "...", "...."]:
        # use \r for a carriage return, use end='' to prevent new line
        print("\r{}{}".format(x, y), end='')
        time.sleep(.25)


# ask for name to put in welcome
# name = input("What is your name?: ")
name = 'Caleb'

# welcome the user and state the motto
print("\nHi {}! Welcome to Lone Peak Credit Union. "
      "You are important to our business!".format(name))

# 0 at the beginning, that changes in the loop
accountBalance = float(conn.execute_read_query('SELECT BALANCE FROM LPCU WHERE USER_ID = 1')[0])

# create loop
while True:

    # ask what action the user wants to take
    action = input("\nWould you like to deposit (d), withdraw (w),\n"
                   "check balance (c), or terminate transaction (t)?: ").lower()

    # if they say deposit, ask how much money and deposit the money into their account
    if action == "d":
        transAmount = float(input("How much money would you like to deposit?: "))
        dot("Depositing")  # call the progress dots function
        accountBalance += transAmount
        print("\nYour balance is now ${:,.2f}".format(accountBalance))

    # if they say withdraw, ask how much and withdraw the money from their account
    elif action == "w":
        transAmount = float(input("How much money would you like to withdraw?: "))

        # if there's enough in the account, pull it. if not, don't.
        if transAmount <= accountBalance:
            dot("Withdrawing")  # call the progress dots function
            accountBalance -= transAmount
            print("\nYour balance is now ${:,.2f}".format(accountBalance))
        else:
            print("Insufficient Funds.\n")

    # if they just want to check balance, print it
    elif action == "c":
        print("Your balance is ${:,.2f}".format(accountBalance))

    elif action == 't':
        break

    # if it's not a correct choice
    else:
        print("Invalid input. Please select deposit or withdraw.")

update_query = 'UPDATE LPCU SET BALANCE = {} WHERE USER_ID = 1'.format(accountBalance)
conn.execute_query(update_query)
conn.close()

print('\nThank you! See you next time.')

# query = '''SELECT BALANCE FROM LPCU WHERE USER_ID = 1;'''
#
#         checkBalance = conn.run_query(query)
#         print("Your balance is ${}".format(checkBalance['BALANCE'][0]))
