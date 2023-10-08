fire_string = input().split('#')
water = int(input())
total_effort = 0
total_fire = 0
print('Cells:')
for fire in fire_string:
    args = fire.split(' = ')
    value = int(args[1])
    valid = False

    if water < value:
        continue
    if args[0] == 'High':
        if 81 <= value <= 125:
            valid = True

    elif args[0] == 'Medium':
        if 51 <= value <= 80:
            valid = True
    elif args[0] == 'Low':
        if 1 <= value <= 50:
            valid = True

    if valid:
        print(f' - {value}')
        water -= value
        total_effort += value * 0.25
        total_fire += value

print(f'Effort: {total_effort:.2f}')
print(f'Total Fire: {total_fire}')


