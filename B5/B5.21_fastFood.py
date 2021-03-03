# Caleb Dillenbeck
# B5 Programming 1 - Mr. Blair
# Fast Food Menu based on Chick-fil-A
# I did not copy anyone

import csv

# Text for the menu.csv:
# Var,Name,Price,Ingredients
# deluxeChickenInfo,Deluxe Chicken Sandwich,3.65,"Chicken, Buns, Pickle, Tomato, Lettuce, Cheese"
# saladInfo,Side Salad,2.89,"Mixed Greens, Cheese, Grape Tomatoes, Bell Peppers, Dressing"
# calebInfo,Caleb,45.00,"Water,People Stuff"


# # Problem 1
# # A
# menu = {}
#
# # B
# menu = {
#     'Chicken Sandwich': 3.05,
#     'Deluxe Chicken Sandwich': 3.65,
#     'Waffle Fries': 1.85,
#     'Shake': 3.15,
#     'Salad': 2.89
# }
#
# # Problem 2
# del menu['Shake']
#
# # Problem 3
# menu['Nuggets'] = 3.05
#
# # Problem 4
# ingredientsMenu = {
#     'Chicken Sandwich': ['Chicken', 'Buns', 'Pickle'],
#     'Deluxe Chicken Sandwich': ['Chicken', 'Buns', 'Pickle', 'Tomato', 'Lettuce', 'Cheese'],
#     'Waffle Fries': ['Potatoes'],
#     'Nuggets': ['Breaded Chicken'],
#     'Salad': ['Mixed Greens', 'Cheese', 'Grape Tomatoes', 'Bell Peppers', 'Dressing']}

# Problem 5/6
# This is built so that you can add more items to the menu from the CSV file
#


# Turns input into an int
def try_block(var):
    try:
        x = int(input(var))
    except ValueError:
        x = None
    return x


# This gets all the info from the CSV file and turns it into dictionaries
def dict_maker(csv_row):
    a_dict = {}
    var_name = csv_row[0]
    name = csv_row[1]
    price = float(csv_row[2])
    ingredients = csv_row[3].split(',')

    # Because I called the variables this way, it says they're unused
    for variable in ['name', 'price', 'ingredients']:
        a_dict[variable.capitalize()] = eval(variable)

    return var_name, a_dict


# Open the file,
with open('menu.csv', newline='\n') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
    next(csvReader)  # Move forward because of the header
    dict_names = []          # This is used to keep track of...
    for row in csvReader:
        y = dict_maker(row)
        vars()[y[0]] = y[1]  # ...the variables named here
        dict_names.append(y[0])

menu = {}

# Add the item dictionaries into the menu dictionary, with numbers as the keys
for names in range(len(dict_names)):
    menu[names + 1] = eval(dict_names[names])

# Options for the console
options = {
    1: 'List the Menu',
    2: 'Add Item to Cart',
    3: 'Remove Item from Cart',
    4: 'List Your Cart',
    5: 'Place Your Order'}

# Print the options
print('Welcome to Chick-fil-A! What can I do for you?')
for key, value in options.items():
    print(f'{key}.) {value}')

order = []
orderPlaced = False

while not orderPlaced:
    prompt = try_block('\nCommand #: ')

    if prompt not in options.keys():
        print('Make sure to input a valid number.')

    # List the menu
    if prompt == 1:
        for key, value in menu.items():
            print(f"{key}.) {value['Name']} - ${value['Price']}")
            print('      Ingredients:')
            for Ingredients in value['Ingredients']:
                print(f'        {Ingredients}')

    # Add item to cart
    elif prompt == 2:
        while True:
            response = try_block('Which item would you like to add to your cart?: ')
            if response not in menu.keys():
                print('Make sure to input a valid number.\n')
            else:
                break
        order.append(menu[response]['Name'])
        print(f'Added a {order[-1]} to cart.')

    # Remove item from cart
    elif prompt == 3:
        if len(order) == 0:
            print('Please add items to your cart first.')
        else:
            response = try_block('Which item would you like to remove from your cart?: ')
            removedItem = order.pop(response - 1)
            print(f'Removed a {removedItem}.')

    # List Cart
    elif prompt == 4:
        if len(order) == 0:
            print('Your cart is empty')
        else:
            print('Your Cart:')
            for item in range(len(order)):
                print(f'  {item + 1}.) {order[item]}')

    # Place order
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
