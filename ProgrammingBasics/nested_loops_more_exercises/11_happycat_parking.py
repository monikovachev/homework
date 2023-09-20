days_total = int(input())
hours_total = int(input())
park_bill = 1
parking_total = 0

for day in range(1, days_total + 1):

    parking_day = 0
    for hour in range(1, hours_total + 1):

        if day % 2 == 0 and hour % 2 != 0:
            parking_day += 2.50
            parking_total += 2.50

        elif day % 2 != 0 and hour % 2 == 0:
            parking_day += 1.25
            parking_total += 1.25

        else:
            parking_day += 1
            parking_total += 1

        if hours_total == hour:
            print(f'Day: {day} - {parking_day:.2f} leva')


print(f'Total: {parking_total:.2f} leva')

