import math

fan_name = input()
budget = float(input())
beer_count = int(input())
chips_count = int(input())

beer_price = 1.20
beer_total = beer_price * beer_count
chips_price = 0.45 * beer_total

total = beer_total + math.ceil(chips_price * chips_count)
diff = abs(budget - total)

if budget >= total:
    print(f'{fan_name} bought a snack and has {diff:.2f} leva left.')
else:
    print(f'{fan_name} needs {diff:.2f} more leva!')

