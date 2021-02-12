# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Fast Food Menu based on Chick-fil-A
# I did not copy anyone


# Problem 1
# A
menu = {}

# B
menu = {'Chicken Sandwich': 3.05, 'Waffle Fries': 1.85,
        'Nuggets': 3.05, 'Salad': 2.89}

# Problem 2
del menu['Nuggets']

# Problem 3
menu['Shake'] = 3.15

# Problem 4
ingredientsMenu = {'Chicken Sandwich': 'Chicken, Buns, Pickle',
                   'Deluxe Chicken Sandwich': 'Chicken, Tomato, Lettuce, Cheese, Buns'}

# Problem 5
options = {
    1: 'List the Menu',
    2: 'Add Item to Cart',
    3: 'Remove Item from Cart',
    4: 'List Your Cart',
    5: 'Place Your Order'}

print('Welcome to Chick-fil-A! What can I do for you?')
for key, value in options.items():
    print(f'{key} - {value}')

while True:
    try:
        prompt = int(input('\nCommand #: '))
    except ValueError:
        prompt = 0
    if prompt != 1 or 2 or 3 or 4 or 5:
        print('Make sure to input a number from 1-5.')

    # FIX ABOVE

    if prompt == 1:
        pass

    elif prompt == 2:
        pass

    elif prompt == 3:
        pass

    elif prompt == 4:
        pass

    elif prompt == 5:
        pass
