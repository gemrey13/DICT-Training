stopper = True
sum = 0
while stopper:
    num = input('Enter a number > ')
    if num.isnumeric():
        sum += int(num)
        continue
    else:
        print(sum)
        break

