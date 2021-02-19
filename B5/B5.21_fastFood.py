# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Fast Food Menu based on Chick-fil-A
# I did not copy anyone

import csv

# Problem 1
# A
menu = {}

# B
menu = {
    'Chicken Sandwich': 3.05,
    'Deluxe Chicken Sandwich': 3.65,
    'Waffle Fries': 1.85,
    'Shake': 3.15,
    'Salad': 2.89}

# Problem 2
del menu['Shake']

# Problem 3
menu['Nuggets'] = 3.05

# Problem 4
ingredientsMenu = {
    'Chicken Sandwich': 'Chicken, Buns, Pickle',
    'Deluxe Chicken Sandwich': 'Chicken, Buns, Pickle, Tomato, Lettuce, Cheese',
    'Waffle Fries': 'Potatoes',
    'Nuggets': 'Breaded Chicken',
    'Salad': 'Mixed Greens, Cheese, Grape Tomatoes, Bell Peppers, Dressing'}


# Problem 5


def try_block(var):
    try:
        x = int(input(var))
    except ValueError:
        x = 0
    return x


deluxeChickenInfo = {
    'Name': 'Deluxe Chicken Sandwich',
    'Price': 3.65,
    'Ingredients': ['Chicken', 'Buns', 'Pickle', 'Tomato', 'Lettuce', 'Cheese']
}

saladInfo = {
    'Name': 'Side Salad',
    'Price': 2.89,
    'Ingredients': ['Mixed Greens', 'Cheese', 'Grape Tomatoes', 'Bell Peppers', 'Dressing']
}

menu = {
    1: deluxeChickenInfo,
    2: saladInfo
}

options = {
    1: 'List the Menu',
    2: 'Add Item to Cart',
    3: 'Remove Item from Cart',
    4: 'List Your Cart',
    5: 'Place Your Order'}

print('Welcome to Chick-fil-A! What can I do for you?')
for key, value in options.items():
    print(f'{key}.) {value}')

order = []
orderPlaced = False

while True:
    try:
        prompt = int(input('\nCommand #: '))
    except ValueError:
        prompt = 0

    if prompt not in options.keys():
        print('Make sure to input a valid number.')
    else:
        int(prompt)

    if prompt == 1:
        for key, value in menu.items():
            print(f"{key}.) {value['Name']} - ${value['Price']}")
            print('      Ingredients:')
            for ingredients in value['Ingredients']:
                print(f'        {ingredients}')

    elif prompt == 2:
        while True:
            response = try_block('Which item would you like to add to your cart?: ')
            if response not in menu.keys():
                print('Make sure to input a valid number.\n')
            else:
                break
        order.append(menu[response]['Name'])
        print(f'Added a {order[-1]} to cart.')

    elif prompt == 3:
        if len(order) == 0:
            print('Please add items to your cart first.')
        else:
            response = try_block('Which item would you like to remove from your cart?: ')
            removedItem = order.pop(response - 1)
            print(f'Removed a {removedItem}.')

    elif prompt == 4:
        if len(order) == 0:
            print('Your cart is empty')
        else:
            print('Your Cart:')
            for item in range(len(order)):
                print(f'  {item + 1}.) {order[item]}')

    elif prompt == 5:
        if len(order) == 0:
            print('Please add items to your cart first.')
        else:
            print('Is your order information correct?:')
            for item in range(len(order)):
                print(f'  {item + 1}.) {order[item]}')
            while True:
                response = input('\n(y/n): ')

                if response == 'y':
                    print('Placing Order...')
                    print('\nOrder Placed. Your food will be ready shortly!')
                    orderPlaced = True
                    order.clear()
                    break
                elif response == 'n':
                    print('Order Cancelled.')
                    break
                else:
                    print("\nPlease input 'y' or 'n'.")
    if orderPlaced:
        break

# Problem 6
print('\n\n---Menu Section---')
with open('menu.csv', 'w+') as menuFile:
    writer = csv.writer(menuFile)
    writer.writerows(menu)
