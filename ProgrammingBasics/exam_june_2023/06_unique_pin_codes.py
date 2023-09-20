cap_first_number = int(input())
cap_second_number = int(input())
cap_third_number = int(input())

for number_1 in range(1, cap_first_number + 1):
    for number_2 in range(2, cap_second_number + 1):
        for number_3 in range(1, cap_third_number + 1):
            if number_1 % 2 == 0 and number_3 % 2 == 0 \
                    and (number_2 == 2 or number_2 == 3 or number_2 == 5 or number_2 == 7):
                print(f'{number_1} {number_2} {number_3}')



