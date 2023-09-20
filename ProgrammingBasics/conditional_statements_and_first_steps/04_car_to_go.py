budget = float(input())
season = input()
class_car = ''
car_type = ''
car_price = 0

if budget <= 100:
    class_car = 'Economy class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.35
    else:
        car_type = 'Jeep'
        car_price = budget * 0.65
elif budget <= 500:
    class_car = 'Compact class'
    if season == 'Summer':
        car_type = 'Cabrio'
        car_price = budget * 0.45
    else:
        car_type = 'Jeep'
        car_price = budget * 0.80
else:
    class_car = 'Luxury class'
    car_type = 'Jeep'
    car_price = budget * 0.90

print(f'{class_car}\n{car_type} - {car_price:.2f}')

