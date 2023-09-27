score = float(input('Enter score > '))
if score > 100:
    print('Excellent!')
elif score > 89:
    print('Good Job!')
elif score > 79:
    print('You\'re doing okay.')
elif score > 69:
    print('You need to work harder.')
else:
    print('You didn\'t pass.')