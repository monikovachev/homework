budget = float(input())
season = input()

place = ''
destination = ''

if season == 'summer':
    place = 'Camp'
else:
    place = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.30
    else:
        price = budget * 0.70

elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.40
    else:
        price = budget * 0.80

else:
    destination = 'Europe'
    place = 'Hotel'
    price = budget * 0.90

print(f'Somewhere in {destination}')
print(f'{place} - {price:.2f}')
