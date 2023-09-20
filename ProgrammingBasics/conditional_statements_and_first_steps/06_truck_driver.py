season = input()
km_monthly = float(input())

price_km = 0

if 10000 < km_monthly <= 20000:
    price_km = 1.45

if season == 'Summer':
    if km_monthly <= 5000:
        price_km = 0.90
    elif km_monthly <= 10000:
        price_km = 1.10
elif season == 'Winter':
    if km_monthly <= 5000:
        price_km = 1.05
    elif km_monthly <= 10000:
        price_km = 1.25
else:
    if km_monthly <= 5000:
        price_km = 0.75
    elif km_monthly <= 10000:
        price_km = 0.95

total_pay = ((km_monthly * price_km) * 4) * 0.90

print(f'{total_pay:.2f}')
