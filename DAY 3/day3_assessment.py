from termcolor import colored
import time as time
contacts = []

def add_contact(name, phone, email):
    dict = {
        'Name': name,
        'Phone Number': phone,
        'Email': email
    }
    contacts.append(dict)
    print(colored('=', 'green') * 70)
    print(colored('\n\tAdded Succesfully!', 'green'))
    print(f"""
            Name          : {name}
            Phone Number  : 09{phone}
            Email Address : {email}
            """)
    time.sleep(2)
    print(colored('=', 'green') * 70)


def display_contacts():
    print(colored('=', 'green') * 70)
    print(colored('\tAll Contacts', 'green'))
    for contact in contacts:
        print(f"""
            Name          : {contact['Name']}
            Phone Number  : 09{contact['Phone Number']}
            Email Address : {contact['Email']}
            """)
        time.sleep(1)
    time.sleep(3)
    print(colored('=', 'green') * 70)


def search_contact(name):
    for contact in contacts:
        if name in contact['Name']:
            print(colored('=', 'green') * 70)
            print(colored('\n\tFound Contact', 'green'))
            print(f"""
            Name          : {contact['Name']}
            Phone Number  : 09{contact['Phone Number']}
            Email Address : {contact['Email']}
            """)
            print(colored('=', 'green') * 70)

            break
    else:
        print(colored('Not Found', 'red'))

def edit_contact(name):
    for contact in contacts:
        if name in contact['Name']:
            print(f"""
            Edit this contact
            Name          : {contact['Name']}
            Phone Number  : 09{contact['Phone Number']}
            Email Address : {contact['Email']}

            Enter a new value for this contact:
            """)
            name = input('Enter a new name > ')
            phone = input('Enter a new phone > 09')
            email = input('Enter a new email > ')

            contact['Name'] = name
            contact['Phone Number'] = phone
            contact['Email'] = email

            print('A contact Edited')
            break
    else:
        print('Not Found')

def remove_contact(name):
    count = 0
    for contact in contacts:
        if name in contact['Name']:
            print('Removed a contact')
            contacts.pop(count)
            break
        else:
            count += 1

def main_menu():
    run = True
    while run:
        print(colored('='*70, 'green'))
        print(colored("""
            Main Menu:
            [A] - Add a new contact
            [B] - Display all contact
            [C] - Search a contact
            [D] - Edit a contact
            [E] - Remove a contact
            [F] - Exit the program
            """, 'green'))
        print(colored('='*70, 'green'))
        
        
        choice = str(input(' >> ')).upper()
        if choice == 'A':
            print(colored(' Enter a Name ', 'green'))
            new_name = str(input(' >> ')).title()
            print(colored(' Enter a Phone Number ', 'green'))
            new_phone = int(input(' >> 09'))
            print(colored(' Enter a Email Address ', 'green'))
            new_email = str(input(' >> '))
            add_contact(new_name, new_phone, new_email)

        elif choice == 'B':
            if contacts:
                display_contacts()
            else:
                print('\n')
                print(colored('='*70, 'red'))
                print(colored('\tNo Available Contacts', 'red') )
                print(colored('='*70, 'red'))


        elif choice == 'C':
            print('Enter a Name ')
            name = str(input(' >> '))
            search_contact(name)
        elif choice == 'D':
            print('Enter a Name ')
            name = str(input(' >> '))
            edit_contact(name)
        elif choice == 'E':
            print('Enter a Name ')
            name = str(input(' >> '))
            remove_contact(name)
        elif choice == 'F':
            break


# add_contact('hehe', 145, 'sdfdsfa@gmail.com')
main_menu()