import random as r
random_integer = r.randint(1,10)
random_string = ''.join(r.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=15))
print(random_integer)
print('h4g{' + random_string + '}')
