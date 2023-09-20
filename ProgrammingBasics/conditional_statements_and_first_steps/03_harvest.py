import math
x = int(input())
y = float(input())
z = int(input())
workers = int(input())

available_wine_acres = x * 0.40

total_kg_grapes = available_wine_acres * y
wine_liters = (total_kg_grapes / 2.5)

leftover = (abs(wine_liters - z))
worker_leftover = math.ceil(leftover / workers)

if wine_liters < z:
    print(f'It will be a tough winter! More {math.floor(leftover)} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(wine_liters)} liters.')
    print(f'{math.ceil(leftover)} liters left -> {worker_leftover} liters per person.')
