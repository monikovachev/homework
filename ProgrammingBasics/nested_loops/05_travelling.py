saved_total = 0

while destination != 'End':
    destination = input()
    min_budget = float(input())

    while min_budget > saved_total:
        saved_cash = float(input())
        saved_total += saved_cash

        if saved_total >= min_budget:
            print(f'Going to {destination}!')
            saved_total = 0
            break



