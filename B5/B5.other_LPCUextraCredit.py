# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Lone Peak Credit Union
# I did not copy anyone but Mr. Blair

# This program simulates an ATM at the newly created Lone Peak Credit Union
# The application supports making deposits and withdrawals from the account
# There is only one account and one user. No password required

import time
import mysql_cursor


# set up function for moving progress dots. functions are fun!!
def dot(x):
    for y in [".", "..", "...", "...."]:
        # use \r for a carriage return, use end='' to prevent new line
        print("\r{}{}".format(x, y), end='')
        time.sleep(.25)


def decimals(num):
    try:
        number = str(num)
        if len(number.rsplit('.')[-1]) == 1:
            return "${:#,}0".format(float(number))
        else:
            return "${:#,}".format(float(number))
    except ValueError:
        return "!!Value Error!!"


# start connection
conn = mysql_cursor.Connection('home.dillenbeck.org', 'caleb', '/.ssh/id_rsa',
                               'caleb', '/sql_pass.txt', 'caleb')

users = conn.execute_read_query("SELECT USER_ID, USER FROM LPCU")

validUser = False

while True:
    name = input("Username: ")
    for _ in users:
        if _[1] == name:
            validUser = True
            user_id = _[0]
            break
    if validUser:
        break
    print('Unknown user. Try again.')

read_password = conn.execute_read_query(f"SELECT USER_ID, PASS FROM LPCU WHERE USER_ID = {user_id}")[0][1]

while True:
    input_password = input("Password: ")
    if input_password == read_password:
        break
    print("Incorrect.")


# welcome the user and state the motto
print("\nHi {}! Welcome to Lone Peak Credit Union. "
      "You are important to our business!".format(name))

# 0 at the beginning, that changes in the loop
accountBalance = float(conn.execute_read_query(
    f'SELECT BALANCE FROM LPCU WHERE USER_ID = {user_id}')[0][0])

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
        print("\nYour balance is now " + decimals(accountBalance))

    # if they say withdraw, ask how much and withdraw the money from their account
    elif action == "w":
        transAmount = float(input("How much money would you like to withdraw?: "))

        # if there's enough in the account, pull it. if not, don't.
        if transAmount <= accountBalance:
            dot("Withdrawing")  # call the progress dots function
            accountBalance -= transAmount
            print("\nYour balance is now " + decimals(accountBalance))
        else:
            print("Insufficient Funds.\n")

    # if they just want to check balance, print it
    elif action == "c":
        print("\nYour balance is " + decimals(accountBalance))

    elif action == 't':
        break

    # if it's not a correct choice
    else:
        print("Invalid input. Please select deposit or withdraw.")

update_query = 'UPDATE LPCU SET BALANCE = {} WHERE USER_ID = {}'.format(accountBalance, user_id)
conn.execute_query(update_query)
conn.close()

print('\nThank you! See you next time.')

# query = '''SELECT BALANCE FROM LPCU WHERE USER_ID = 1;'''
#
#         checkBalance = conn.run_query(query)
#         print("Your balance is ${}".format(checkBalance['BALANCE'][0]))
