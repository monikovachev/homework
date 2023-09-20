month = input()
total_nights = int(input())

studio_price = 0
apartment_price = 0

if month == 'May' or month == 'October':
    studio_price = 50
    apartment_price = 65
    if total_nights > 14:
        studio_price = studio_price * 0.70
    elif total_nights > 7:
        studio_price = studio_price * 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.20
    apartment_price = 68.70
    if total_nights > 14:
        studio_price = studio_price * 0.80
else:
    studio_price = 76
    apartment_price = 77

if total_nights > 14:
    apartment_price = apartment_price * 0.90

checkout_aps = total_nights * apartment_price
checkout_studio = total_nights * studio_price

print(f'Apartment: {checkout_aps:.2f} lv.')
print(f'Studio: {checkout_studio:.2f} lv.')
