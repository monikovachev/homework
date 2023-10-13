def sum_of_even_and_odd(number):
    sum_even = 0
    sum_odd = 0
    list_as_digits = list(map(int, str(number)))

    for digit in list_as_digits:
        if digit % 2 == 0:
            sum_even += digit
        else:
            sum_odd += digit

    return f'Odd sum = {sum_odd}, Even sum = {sum_even}'


number_given = int(input())

print(sum_of_even_and_odd(number_given))
