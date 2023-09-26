N = int(input())
highest_value = 0

for snowball in range(N):

    weight = int(input())
    time_needed = int(input())
    quality = int(input())

    value = (weight / time_needed) ** quality

    if value >= highest_value:
        highest_value = value
        peak_weight = weight
        peak_time = time_needed
        peak_quality = quality

print(f'{peak_weight} : {peak_time} = {int(highest_value)} ({peak_quality})')