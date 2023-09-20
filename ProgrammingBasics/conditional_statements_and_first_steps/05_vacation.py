budget = float(input())
season = input()
type_stay = ''
place = ''

if budget <= 1000:
    type_stay = 'Camp'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.65
    else:
        place = 'Morocco'
        price = budget * 0.45
elif budget <= 3000:
    type_stay = 'Hut'
    if season == 'Summer':
        place = 'Alaska'
        price = budget * 0.80
    else:
        place = 'Morocco'
        price = budget * 0.60
else:
    type_stay = 'Hotel'
    price = budget * 0.90
    if season == 'Summer':
        place = 'Alaska'
    else:
        place = 'Morocco'

print(f'{place} - {type_stay} - {price:.2f}')
