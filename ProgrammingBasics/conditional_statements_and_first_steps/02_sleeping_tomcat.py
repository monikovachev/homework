from math import floor

daily_play_work = 63
daily_play_rest = 127
normal_yearly_play = 30000

rest_days_total = int(input())

work_days_minutes = (365 - rest_days_total) * daily_play_work

total_play_time = rest_days_total * daily_play_rest + work_days_minutes
difference = abs(normal_yearly_play - total_play_time)
difference_hours = floor(difference / 60)
difference_minutes = difference - (difference_hours * 60)

if total_play_time > normal_yearly_play:
    print(f'Tom will run away')
    print(f'{difference_hours} hours and {difference_minutes} minutes more for play')
else:
    print(f'Tom sleeps well')
    print(f'{difference_hours} hours and {difference_minutes} minutes less for play')