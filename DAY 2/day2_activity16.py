fruits = []

run = True
while run:
    a_fruit = str(input('Enter a Fruit > '))

    if a_fruit in fruits:
        print('Already in list')
        continue

    elif a_fruit.lower() == 'stop':
        print('Loop Terminated')
        run = False
        break

    else:
        fruits.append(a_fruit.capitalize())
        print('fruit added\n')

print(fruits)