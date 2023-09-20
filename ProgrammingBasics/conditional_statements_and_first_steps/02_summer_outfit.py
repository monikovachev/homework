degrees = int(input())
time_day = input()

outfit = ['Sweatshirt', 'Shirt', 'T-Shirt', 'Swim Suit']
shoes = ['Sneakers', 'Moccasins', 'Barefoot', 'Sandals']

if 10 <= degrees <= 18:
    if time_day == 'Morning':
        outfit = outfit[0]
        shoes = shoes[0]
    elif time_day == 'Afternoon':
        outfit = outfit[1]
        shoes = shoes[1]
    else:
        outfit = outfit[1]
        shoes = shoes[1]
elif 18 < degrees <= 24:
    if time_day == 'Morning':
        outfit = outfit[1]
        shoes = shoes[1]
    elif time_day == 'Afternoon':
        outfit = outfit[2]
        shoes = shoes[3]
    else:
        outfit = outfit[1]
        shoes = shoes[1]
else:
    if time_day == 'Morning':
        outfit = outfit[2]
        shoes = shoes[3]
    elif time_day == 'Afternoon':
        outfit = outfit[3]
        shoes = shoes[2]
    else:
        outfit = outfit[1]
        shoes = shoes[1]

print(f'It\'s {degrees} degrees, get your {outfit} and {shoes}.')