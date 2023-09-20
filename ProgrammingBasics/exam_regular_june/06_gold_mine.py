locations_count = int(input())


for locations in range(locations_count):
    expected_avg_gold = float(input())
    days_spent = int(input())
    gold_total = 0

    for day in range(days_spent):
        gold_per_day = float(input())
        gold_total += gold_per_day

    actual_avg = gold_total / days_spent

    if actual_avg >= expected_avg_gold:
        print(f'Good job! Average gold per day: {actual_avg:.2f}.')
    else:
        print(f'You need {expected_avg_gold - actual_avg:.2f} gold.')

