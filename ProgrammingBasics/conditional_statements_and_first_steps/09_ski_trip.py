ROOM = 18
APARTMENT = 25
PRESIDENTIAL_APARTMENT = 35

days_staying = int(input())
type_room = input()
grade = input()

discount = 1

if type_room == 'apartment':
    if days_staying < 10:
        discount = 0.70
    elif days_staying <= 15:
        discount = 0.65
    else:
        discount = 0.50
elif type_room == 'president apartment':
    if days_staying < 10:
        discount = 0.90
    elif days_staying <= 15:
        discount = 0.85
    else:
        discount = 0.80

total_price_apartment = ((days_staying - 1) * APARTMENT) * discount
total_price_room = (days_staying - 1) * ROOM
total_price_president_room = ((days_staying - 1) * PRESIDENTIAL_APARTMENT) * discount

if type_room == 'apartment':
    if grade == 'positive':
        final_price = total_price_apartment * 1.25
    else:
        final_price = total_price_apartment * 0.90
elif type_room == 'president apartment':
    if grade == 'positive':
        final_price = total_price_president_room * 1.25
    else:
        final_price = total_price_president_room * 0.90
else:
    if grade == 'positive':
        final_price = total_price_room * 1.25
    else:
        final_price = total_price_room * 0.90

print(f'{final_price:.2f}')
