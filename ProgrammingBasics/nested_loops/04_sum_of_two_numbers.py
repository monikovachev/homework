interval_start = int(input())
interval_stop = int(input())
magic_number = int(input())
combination = 0
is_found = False

for first_number in range(interval_start, interval_stop + 1):
    for second_number in range(interval_start, interval_stop + 1):
        combination += 1
        if first_number + second_number == magic_number:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f'Combination N:{combination} ({first_number} + {second_number} = {magic_number})')
else:
    print(f'{combination} combinations - neither equals {magic_number}')
