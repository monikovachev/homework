from math import floor
tournaments = int(input())
initial_points = int(input())
total_points = initial_points
wins = 0

for _ in range(tournaments):
    placed = input()
    if placed == 'W':
        total_points += 2000
        wins += 1
    elif placed == 'F':
        total_points += 1200
    else:
        total_points += 720

    pcg_wins = wins / tournaments * 100

avg_points = (total_points-initial_points) / tournaments

print(f'Final points: {total_points}\nAverage points: {floor(avg_points)}\n{pcg_wins:.2f}%')

