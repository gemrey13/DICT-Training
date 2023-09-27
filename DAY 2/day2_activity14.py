odd = 0
even = 0
count = 1
odd_list = ''
even_list = ''
for i in range(10):
    num = int(input(f'enter #{count} > '))
    count += 1
    if (num % 2) == 0:
        even += 1
        if count == 9:
            even_list += f'{num}'
        else:
            even_list += f'{num}, '

    else:
        odd += 1
        if count == 9:
            odd_list += f'{num}'
        else:
            odd_list += f'{num}, '

even_msg = f'There is {even} EVEN number - {even_list}' if even == 1 else f'There are {even} EVEN numbers - {even_list}'
odd_msg = f'There is {odd} ODD number - {odd_list}' if odd == 1 else f'There are {odd} ODD numbers - {odd_list}'

print(even_msg)
print(odd_msg)