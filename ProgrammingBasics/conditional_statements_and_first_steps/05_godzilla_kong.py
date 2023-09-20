movie_budget = float(input())
statist_count = int(input())
clothes_price_per_statist = float(input())

decoration = movie_budget * 0.10
statist_total = statist_count * clothes_price_per_statist

leftover = abs((decoration + statist_total) - movie_budget)

if statist_count > 150:
    statist_total = statist_total - statist_total * 0.10

if decoration + statist_total > movie_budget:
    print(f'Not enough money!')
    print(f'Wingard needs {leftover:.2f} leva more.')

if decoration + statist_total <= movie_budget:
    print(f'Action!')
    print(f'Wingard starts filming with {leftover:.2f} leva left.')
