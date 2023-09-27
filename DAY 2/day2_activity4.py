print('select a temperature f - fahrenheit, c - celsius')
choice = str(input('> ')).lower()
print('Enter a temperature')
temp = float(input('> '))
if choice == 'c':
    fahrenheit = (temp * 9 / 5) + 32
    print(f'{fahrenheit}f')
elif choice == 'f':
    celsius = (temp - 32) * 5 / 9
    print(f'{celsius}c')
else:
    print('no choices')

