world_record = float(input())
distance = float(input())
seconds_per_meter = float(input())

ivan_time_no_resistance = seconds_per_meter * distance

ivan_time = ivan_time_no_resistance + (distance // 15) * 12.5

leftover = abs(world_record - ivan_time)

if ivan_time < world_record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
elif ivan_time >= world_record:
    print(f'No, he failed! He was {leftover:.2f} seconds slower.')