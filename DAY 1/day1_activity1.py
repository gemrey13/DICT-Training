print('*\n* *\n* * *\n* * * *\n* * * * *')

from random import random
import time as t

print('*' * 10)
a = int(input('choose number 1 - 6 > '))
bullet = int(random() * 6)
t.sleep(4)
if a == bullet:
    print('Your dead!')
else:
    print('Safe')
print(bullet)

