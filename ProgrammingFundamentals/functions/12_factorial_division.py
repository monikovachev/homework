from math import factorial


def factorial_division(first, second):

    result = factorial(first) / factorial(second)
    return f'{result:.2f}'


first_number = int(input())
second_number = int(input())

print(factorial_division(first_number, second_number))
