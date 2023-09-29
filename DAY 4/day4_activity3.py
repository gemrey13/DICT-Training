
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None
    else:
        return result
    finally:
        print('Program Finished')

result = divide(12, 0)

print(result)

