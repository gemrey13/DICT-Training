gross = float(input("Enter gross salary > "))
deduction = float(input("Enter deduction > "))
name = str(input("Enter full name > "))

netPay = gross - deduction
print(f'Hi Sir {name.upper()} based on the provided information your net pay is {netPay}')