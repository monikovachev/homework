def is_perfect(number):
    divisor_sum = 0
    for divisor in range(1, number):
        if number % divisor == 0:
            divisor_sum += divisor

    if divisor_sum == number:
        return 'We have a perfect number!'
    return 'It\'s not so perfect.'


given_number = int(input())
print(is_perfect(given_number))
