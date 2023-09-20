capacity_total = float(input())
round = 1
suitcase_total = 0
current_suitcase = 0

while True:
    command = input()
    if command == 'End':
        break
    current_suitcase = float(command)
    if round % 3 == 0:
        current_suitcase *= 1.10
    if current_suitcase > capacity_total:
        break

    round += 1
    capacity_total -= current_suitcase
    suitcase_total += 1


if command == 'End':
    print('Congratulations! All suitcases are loaded!')
elif current_suitcase > capacity_total:
    print('No more space!')
print(f'Statistic: {suitcase_total} suitcases loaded.')


