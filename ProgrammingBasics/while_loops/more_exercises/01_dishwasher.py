bottle_count = int(input())
bottle_total = bottle_count * 750
round = 1
command = input()
washed_total = 0
washed_plates = 0
washed_pans = 0
is_left = False

while bottle_total >= washed_total:
    if command == 'End':
        is_left = True
        break

    if round % 3 == 0:
        washed_pans += int(command)
        washed_total += int(command) * 15
    else:
        washed_plates += int(command)
        washed_total += int(command) * 5

    if washed_total > bottle_total:
        break

    round += 1
    command = input()

if is_left:
    print(f'Detergent was enough!')
    print(f'{washed_plates} dishes and {washed_pans} pots were washed.')
    print(f'Leftover detergent {bottle_total - washed_total} ml.')
else:
    print(f'Not enough detergent, {washed_total - bottle_total} ml. more necessary!')
