hour_exam = int(input())
minutes_exam = int(input())
hour_arrival = int(input())
minutes_arrival = int(input())

total_exam_in_minutes = hour_exam * 60 + minutes_exam
total_arrival_in_minutes = hour_arrival * 60 + minutes_arrival

difference_minutes = abs(total_exam_in_minutes - total_arrival_in_minutes)

if total_arrival_in_minutes > total_exam_in_minutes:
    print('Late')
elif total_exam_in_minutes - total_arrival_in_minutes <= 30:
    print('On time')
else:
    print('Early')

if total_exam_in_minutes - total_arrival_in_minutes > 0:
    if difference_minutes < 60:
        print(f'{difference_minutes} minutes before the start')
    else:
        print(f'{difference_minutes // 60}:{difference_minutes % 60:02d} hours before the start')
elif total_arrival_in_minutes - total_exam_in_minutes > 0:
    if difference_minutes < 60:
        print(f'{difference_minutes} minutes after the start')
    else:
        print(f'{difference_minutes // 60}:{difference_minutes % 60:02d} hours after the start')