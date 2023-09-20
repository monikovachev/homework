import math

tv_series = str(input())
episode_length = int(input())
break_length = int(input())

lunch_time = break_length * 1/8
lunch_air = break_length * 0.25

time_to_watch = break_length - (lunch_time + lunch_air)
leftover = math.ceil(abs(time_to_watch - episode_length))

if int(time_to_watch) >= episode_length:
    print(f'You have enough time to watch {tv_series} and left with {leftover} minutes free time.')
else:
    print(f'You don\'t have enough time to watch {tv_series}, you need {leftover} more minutes.')
