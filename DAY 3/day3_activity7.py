def calculate(num1, num2, operator):
    if operator == 'add':
        return num1 + num2
    elif operator == 'minus':
        return num1 - num2
    elif operator == 'divide':
        return num1 / num2
    elif operator == 'times':
        return num1 * num2
    else:
        return 'ERROR: Invalid'
    


print("""
    Enter the First Number :
""")
num1 = float(input('>> '))
print("""
    Enter the Second Number :
""")
num2 = float(input('>> '))
print("""
    Select Operator:
      [add] - Addition
      [minus] - Subtraction
      [divide] - Division
      [times] - Multiplication
    """)
operator = input('>> ')


print(calculate(num1, num2, operator))