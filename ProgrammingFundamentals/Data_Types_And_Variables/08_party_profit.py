from math import floor
group_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):

    if day % 10 == 0:
        group_size -= 2

    if day % 15 == 0:
        group_size += 5

    coins += (group_size * -2) + 50

    if day % 3 == 0:
        coins -= group_size * 3

    if day % 5 == 0:
        if day % 3 == 0:
            coins -= group_size * 2

        coins += group_size * 20

coins_per_companion = floor(coins / group_size)
print(f'{group_size} companions received {coins_per_companion} coins each.')

