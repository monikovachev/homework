from math import floor

biscuits_per_day_and_worker = int(input())
workers_count = int(input())
competing_factory_biscuits = int(input())

daily_biscuits = biscuits_per_day_and_worker * workers_count

monthly_produced_biscuits = 20 * daily_biscuits + 10 * floor(daily_biscuits * 0.75)

print(f'You have produced {monthly_produced_biscuits} biscuits for the past month.')

if competing_factory_biscuits > monthly_produced_biscuits:
    percentage_difference = (competing_factory_biscuits - monthly_produced_biscuits) / competing_factory_biscuits * 100
    print(f'You produce {percentage_difference:.2f} percent less biscuits.')
else:
    percentage_difference = (monthly_produced_biscuits - competing_factory_biscuits) / competing_factory_biscuits * 100
    print(f'You produce {percentage_difference:.2f} percent more biscuits.')
