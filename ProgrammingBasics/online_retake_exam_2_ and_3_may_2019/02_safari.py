liter_gas = 2.10
tax_excursionist = 100

budget = float(input())
needed_gas_liters = float(input())
day = input()
total = needed_gas_liters * liter_gas + 100

if day == 'Saturday':
    total *= 0.90
else:
    total *= 0.80

if budget >= total:
    print(f'Safari time! Money left: {budget - total:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total - budget:.2f} lv.')