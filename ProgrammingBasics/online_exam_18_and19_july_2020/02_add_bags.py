luggage_over_20kg = float(input())
luggage_weight = float(input())
days_until_flight = int(input())
luggage_count = int(input())
price = luggage_over_20kg

if luggage_weight < 10:
    price = luggage_over_20kg * 0.20
elif luggage_weight <= 20:
    price = luggage_over_20kg * 0.50

if days_until_flight > 30:
    price *= 1.10
elif days_until_flight < 7:
    price *= 1.40
else:
    price *= 1.15

total = luggage_count * price

print(f'The total price of bags is: {total:.2f} lv.')
