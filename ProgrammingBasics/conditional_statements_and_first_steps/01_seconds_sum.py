from math import floor

racer_1 = int(input())
racer_2 = int(input())
racer_3 = int(input())

total_time = racer_1 + racer_2 + racer_3

time_in_minutes = total_time / 60
time_in_second = total_time % 60

time_in_minutes = floor(time_in_minutes)

if time_in_second < 10:
    print(f"{time_in_minutes}:0{time_in_second}")
else:
    print(f"{time_in_minutes}:{time_in_second}")
