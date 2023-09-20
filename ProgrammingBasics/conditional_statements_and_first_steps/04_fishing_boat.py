budget = int(input())
season = input()
fishermen = int(input())

if season == 'Spring':
    if fishermen <= 6:
        rent = 3000 * 0.90
    elif 7 <= fishermen <= 11:
        rent = 3000 * 0.85
    else:
        rent = 3000 * 0.75
elif season == 'Winter':
    if fishermen <= 6:
        rent = 2600 * 0.90
    elif 7 <= fishermen <= 11:
        rent = 2600 * 0.85
    else:
        rent = 2600 * 0.75
else:
    if fishermen <= 6:
        rent = 4200 * 0.90
    elif 7 <= fishermen <= 11:
        rent = 4200 * 0.85
    else:
        rent = 4200 * 0.75


if fishermen % 2 == 0 and season != 'Autumn':
    rent = rent * 0.95

leftover = abs(budget - rent)

if budget >= rent:
    print(f'Yes! You have {leftover:.2f} leva left.')
else:
    print(f'Not enough money! You need {leftover:.2f} leva.')


