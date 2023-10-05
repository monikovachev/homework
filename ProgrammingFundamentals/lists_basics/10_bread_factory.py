event_string = input().split('|')
energy = 100
coins = 100
has_managed_all_events = True

for event in event_string:

    current_event = event.split('-')
    type = current_event[0]
    number = int(current_event[1])

    if type == 'rest':
        current_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        number_gained = energy - current_energy
        print(f'You gained {number_gained} energy.')
        print(f'Current energy: {energy}.')

    elif type == 'order':
        if energy >= 30:
            print(f'You earned {number} coins.')
            energy -= 30
            coins += number
        else:
            energy += 50
            print(f'You had to rest!')
    else:
        if coins >= number:
            print(f'You bought {type}.')
            coins -= number
        else:
            print(f'Closed! Cannot afford {type}.')
            has_managed_all_events = False
            break

if has_managed_all_events:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
