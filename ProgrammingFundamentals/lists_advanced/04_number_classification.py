def positive_numbers(list_numbers):
    return ', '.join([number for number in list_numbers if int(number) >= 0])


def negative_numbers(list_numbers):
    return ', '.join([number for number in list_numbers if int(number) < 0])


def even_numbers(list_numbers):
    return ', '.join([number for number in list_numbers if int(number) % 2 == 0])


def odd_numbers(list_numbers):
    return ', '.join([number for number in list_numbers if int(number) % 2 != 0])


numbers_list = input().split(', ')

print(f'Positive: {positive_numbers(numbers_list)}')
print(f'Negative: {negative_numbers(numbers_list)}')
print(f'Even: {even_numbers(numbers_list)}')
print(f'Odd: {odd_numbers(numbers_list)}')
