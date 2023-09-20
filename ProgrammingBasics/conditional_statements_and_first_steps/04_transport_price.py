n = int(input())
time_of_travel = str(input())

taxi_day = 0.79 * n + 0.70
taxi_night = 0.90 * n + 0.70
bus = 0.09 * n
train = 0.06 * n

if n < 20:
    if time_of_travel == 'day':
        print(f'{taxi_day:.2f}')
    elif time_of_travel == 'night':
        print(f'{taxi_night:.2f}')

elif n < 100:
    print(f'{bus:.2f}')
else:
    print(f'{train:.2f}')
