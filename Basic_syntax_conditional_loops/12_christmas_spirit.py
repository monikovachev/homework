decorations_quantity = int(input())
days_until_christmas = int(input())
spirit_points = 0
total_cost = 0

for day in range(1, days_until_christmas + 1):

    if day % 11 == 0:
        decorations_quantity += 2

    if day % 2 == 0:
        spirit_points += 5
        total_cost += 2 * decorations_quantity

    if day % 3 == 0:
        spirit_points += 13
        total_cost += 8 * decorations_quantity

    if day % 5 == 0:
        spirit_points += 17
        total_cost += 15 * decorations_quantity

        if day % 3 == 0:
            spirit_points += 30

    if day % 10 == 0:
        spirit_points -= 20
        total_cost += 23

if days_until_christmas % 10 == 0:
    spirit_points -= 30


print(f'Total cost: {total_cost}')
print(f'Total spirit: {spirit_points}')
