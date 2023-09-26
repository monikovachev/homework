water_tank = 0
n = int(input())

for _ in range(n):

    liters_water = int(input())

    if liters_water + water_tank > 255:
        print(f'Insufficient capacity!')
        continue

    water_tank += liters_water

print(water_tank)
