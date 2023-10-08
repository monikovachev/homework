items = input().split('|')
given_budget = float(input())
profit = 0
expenses = 0
new_prices = []
for item in items:
    args = item.split('->')
    product = args[0]
    price = float(args[1])
    is_valid = False

    if price > given_budget:
        continue

    if product == 'Clothes':
        if price > 50:
            continue
        is_valid = True

    elif product == 'Shoes':
        if price > 35:
            continue
        is_valid = True

    elif product == 'Accessories':
        if price > 20.50:
            continue
        is_valid = True

    if is_valid:
        given_budget -= price
        sell_price = price * 1.40
        new_prices.append(sell_price)
        profit += sell_price
        expenses += price
        print(f'{sell_price:.2f}', end=' ')

profit -= expenses
print()
print(f'Profit: {profit:.2f}')

if given_budget + sum(new_prices) >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')
