number = int(input())
sum_needed = 0

for result in range(1111, 10_000):
    is_special = True
    for index, digit in enumerate(str(result)):

        if int(digit) == 0:
            is_special = False
            break

        if not number % int(digit) == 0:
            is_special = False
            break
    if is_special:
        print(result, end=' ')

