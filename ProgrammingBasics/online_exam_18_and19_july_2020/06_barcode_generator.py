first_number = int(input())
second_number = int(input())

first_start = int(first_number / 1000)
second_start = int((first_number / 100) % 10)
third_start = int((first_number / 10) % 10)
fourth_start = int(first_number % 10)

first_end = int(second_number / 1000)
second_end = int((second_number / 100) % 10)
third_end = int((second_number / 10) % 10)
fourth_end = int(second_number % 10)

for num_1 in range(first_start, first_end + 1):
    for num_2 in range(second_start, second_end + 1):
        for num_3 in range(third_start, third_end + 1):
            for num_4 in range(fourth_start, fourth_end + 1):
                if num_1 % 2 != 0 and num_2 % 2 != 0 and num_3 % 2 != 0 and num_4 % 2 != 0:
                    print(f'{num_1}{num_2}{num_3}{num_4}', end=' ')

