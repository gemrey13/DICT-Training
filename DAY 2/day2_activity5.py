age = input('Enter age > ')
if age.isnumeric():
    age = int(age)
    if age <= 12 and age > 0:
        print('CHILD')
    elif age <= 19:
        print('TEEN')
    elif age <= 64:
        print('ADULT')
    else:
        print('SENIOR')
else:
    print('OBOBO')