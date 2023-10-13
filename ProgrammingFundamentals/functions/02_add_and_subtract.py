def sum_numbers(first, second):
    result = first + second
    return result


def subtract(result, third):

    return result - third


def add_and_subtract(first, second, third):
    result = sum_numbers(first, second)
    final_result = subtract(result, third)
    return final_result


first_number = int(input())
second_number = int(input())
third_number = int(input())
print(add_and_subtract(first_number, second_number, third_number))
