days_count = int(input())
hours = int(input())
day_total = 0
total = 0

for day in range(1, days_count + 1):
    day_total = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and not hour % 2 == 0:
            price = 2.50
        elif not day % 2 == 0 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1

        day_total += price
        total += price
    print(f'Day: {day} - {day_total:.2f} leva')

print(f'Total: {total:.2f} leva')