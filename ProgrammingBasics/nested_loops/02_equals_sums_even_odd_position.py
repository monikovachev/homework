number_1 = int(input())
number_2 = int(input())

for number in range(number_1, number_2 + 1):
    number_str = str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end=' ')
