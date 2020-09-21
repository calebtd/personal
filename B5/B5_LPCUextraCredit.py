# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Lone Peak Credit Union
# I did not copy anyone but Mr. Blair

# This program simulates an ATM at the newly created Lone Peak Credit Union
# The application supports making deposits and withdrawals from the account
# There is only one account and one user. No password required


# welcome the user and state the motto
print("Welcome to Lone Peak Credit Union! You are important to our business!")
accountBalance = 0.0

# create loop
while True:

    # ask what action the user wants to take
    action = input("Would you like to deposit (d), or withdraw (w)?: ").lower()

    # clean up other inputs
    if action == 'deposit':
        action = 'd'
    elif action == 'withdraw':
        action = 'w'

    # if they say deposit, ask how much money and deposit the money into their account
    if action == "d":
        transAmount = float(input("How much money would you like to deposit?: "))
        accountBalance += transAmount

    # if they say withdraw, ask how much and withdraw the money from their account
    elif action == "w":
        transAmount = float(input("How much money would you like to withdraw?: "))

        if transAmount <= accountBalance:
            accountBalance

    # print out the balance in their account
    print("Your balance is ${:,.2f}".format(accountBalance))

    # if it's not a correct choice
    else:
        print("Please select deposit or withdraw.")
