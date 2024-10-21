## This program will simulate an ordering system
# The program will allow the user to oder 4 items from a menu
# They will be able to stop ordering by pressing number 5

# Printing the welcome message for the user
print("Welcome to Taco Palace, please view the menu below "
      "and enter the number that represents your selection.")


# the menu function
def taco_menu(index):
    menu = [
        "1. Taco",
        "2. Burrito",
        "3. Nachos",
        "4. Soft Drink",
        "5. Quit",
    ]
    print(taco_menu(1))

# Asking the user for their desired item
order = input('What is your desired item? \n')

quit = 5

# Printing the user's option
print('You have selected: ' + order)

while order != quit:
    print('You have selected:' + order)
    if (order == 1):
        print('You ordered a Taco.')
    elif order == 2:
        print('You ordered a Burrito')
    elif order == 3:
        print('You ordered a Nachos')
    elif order == 4:
        print('Soft Drink')
    else:
        print('Thank you for ordering and have a good day :)')


#while menuInput != 5:
#    print('Your oder is')