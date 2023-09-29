"""
Library for calculator\n
add()\n
divide()\n
subtract()\n
multiply()\n
modulo()\n
"""
import math


def add(x, y):
    """
    add the num
    """
    return x + y

def subtract(x, y):
    """
    subtract the num
    """
    return x - y

def divide(x, y):
    """
    divide the num
    """
    return x / y

def multiply(x, y):
    """
    multiply the num
    """
    return x * y

def modulo(x, y):
    """
    modulo of the num
    """
    return x % y

def floor_division(x, y):
    return x // y

def power(x, y):
    return x ** y

def circumference(x, y):
    return x * math.pi * y

def summation(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i

    return sum

def factorial(num: int):
    factorial = 1
    for x in range(1, num + 1):
        factorial *= x
    
    return factorial