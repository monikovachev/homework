from math import floor

balls_count = int(input())
points = 0
other = 0
red_count = 0
orange_count = 0
yellow_count = 0
white_count = 0
black_count = 0
for ball in range(balls_count):
    color = input()
    if color == 'red':
        red_count += 1
        points += 5
    elif color == 'orange':
        orange_count += 1
        points += 10
    elif color == 'yellow':
        yellow_count += 1
        points += 15
    elif color == 'white':
        white_count += 1
        points += 20
    elif color == 'black':
        black_count += 1
        points = floor(points / 2)
    else:
        other += 1
        continue

print(f'Total points: {points}')
print(f'Red balls: {red_count}')
print(f'Orange balls: {orange_count}')
print(f'Yellow balls: {yellow_count}')
print(f'White balls: {white_count}')
print(f'Other colors picked: {other}')
print(f'Divides from black balls: {black_count}')
