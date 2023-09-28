import time as t
from termcolor import colored
grocery_list = []
run = True

def display_grocery():
    print('\n\tGrocery List:')
    count = 0
    for grocery in grocery_list:
        count += 1
        t.sleep(1)
        print(f'\t[Item#{count}] - {grocery}')
        t.sleep(1)

def add_grocery():
    print('\tAdd a Grocery Item')
    item = str(input(">> "))
    grocery_list.append(item)
    t.sleep(2)
    print(f'\n\t{item} Item Added')

def remove_grocery():
    print('\tRemove a Grocery Item')
    item = str(input(">> "))
    if item in grocery_list:
        grocery_list.remove(item)
        print(f'\n\t{item} Item Removed')
    else:
        print('There\'s no item in the Grocery List.')
    t.sleep(2)

def exit_program():
    t.sleep(1)
    print('\tPlease wait!!')
    t.sleep(2)
    print('\tProgram Stopped')

def start_up():
    t.sleep(1)
    print(colored('\tPlease Wait.....', 'green'))
    t.sleep(1)
    print(colored('\tStarting Program...... ', 'green'))
    t.sleep(2)
    print(colored('\tPlease Wait.....', 'green'))
    t.sleep(1)



start_up()
while run:
    print(colored("""
        MENU:
          [1] - Print Grocery List
          [2] - Add Item in Grocery List
          [3] - Remove an Item in Grocery List
          [4] - Exit
        """, 'blue'))
    
    choice = input('>> ')
    if choice.isnumeric():
        choice = int(choice)
        if choice == 1:
            display_grocery()
        elif choice == 2:
            add_grocery()
        elif choice == 3:
            remove_grocery()
        elif choice == 4:
            exit_program()
            run = False
        else:
            print('Please Enter a valid choice')
    else:
        print('Please Enter a number')
