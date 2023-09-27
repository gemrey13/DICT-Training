# money = int(input('Enter a amount > '))

# thousand =     money // 1000
# fiveHundred = (money % 1000 ) // 500
# twoHundred = ((money % 1000 ) % 500) // 200
# hundred =   (((money % 1000 ) % 500) % 200) // 100
# fifty =    ((((money % 1000 ) % 500) % 200) % 100) // 50
# twenty =  (((((money % 1000 ) % 500) % 200) % 100) % 50) // 20
# ten =    ((((((money % 1000 ) % 500) % 200) % 100) % 50) % 20) // 10
# five =  (((((((money % 1000 ) % 500) % 200) % 100) % 50) % 20) % 10) // 5
# one =  ((((((((money % 1000 ) % 500) % 200) % 100) % 50) % 20) % 10) % 5) // 1

# print(f"""
#     {thousand} - 1000
#     {fiveHundred} - 500
#     {twoHundred} - 200
#     {hundred} - 100
#     {fifty} - 50
#     {twenty} - 20
#     {ten} - 10
#     {five} - 5
#     {one} - 1
# """)


pera = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
peraMo = int(input('>>> '))
for i in pera:
    count = peraMo // i
    print(f'{i} -----------  {count}')
    peraMo = peraMo % i