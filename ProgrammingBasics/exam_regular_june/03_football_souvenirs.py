team = input()
souvenir_type = input()
souvenir_count = int(input())
price = 0

if team == 'Argentina':
    if souvenir_type == 'flags':
        price = 3.25
    elif souvenir_type == 'caps':
        price = 7.20
    elif souvenir_type == 'posters':
        price = 5.10
    elif souvenir_type == 'stickers':
        price = 1.25
    else:
        print('Invalid stock!')
elif team == 'Brazil':
    if souvenir_type == 'flags':
        price = 4.20
    elif souvenir_type == 'caps':
        price = 8.50
    elif souvenir_type == 'posters':
        price = 5.35
    elif souvenir_type == 'stickers':
        price = 1.20
    else:
        print('Invalid stock!')
elif team == 'Croatia':
    if souvenir_type == 'flags':
        price = 2.75
    elif souvenir_type == 'caps':
        price = 6.90
    elif souvenir_type == 'posters':
        price = 4.95
    elif souvenir_type == 'stickers':
        price = 1.10
    else:
        print('Invalid stock!')
elif team == 'Denmark':
    if souvenir_type == 'flags':
        price = 3.10
    elif souvenir_type == 'caps':
        price = 6.50
    elif souvenir_type == 'posters':
        price = 4.80
    elif souvenir_type == 'stickers':
        price = 0.90
    else:
        print('Invalid stock!')
else:
    print('Invalid country!')

total = souvenir_count * price
if price != 0:
    print(f'Pepi bought {souvenir_count} {souvenir_type} of {team} for {total:.2f} lv.')

