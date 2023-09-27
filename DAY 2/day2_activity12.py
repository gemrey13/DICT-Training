# import time as t
# i = 1
# while True:
#     print(i)
#     i += 1
#     t.sleep(1)

tuloy = True

while tuloy:
    name = input('Enter a name > ')
    if name == 'stop':
        print('Stopped!!')
        tuloy = False
        break
    else:
        continue