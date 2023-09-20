# Solution 1

charity_raise = int(input())
total_sold = 0
total_cash = 0
total_card = 0
round = 1
has_raised = False
cash = 0
cards = 0
command = input()

while charity_raise >= total_sold:
    if command == 'End':
        print(f'Failed to collect required money for charity.')
        break

    if round % 2 == 1:
        if int(command) <= 100:
            total_sold += int(command)
            total_cash += int(command)
            cash += 1
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')
    else:
        if int(command) > 10:
            total_sold += int(command)
            total_card += int(command)
            cards += 1
            print(f'Product sold!')
        else:
            print(f'Error in transaction!')

    if total_sold >= charity_raise:
        has_raised = True
        break

    round += 1
    command = input()

if has_raised:
    print(f'Average CS: {total_cash / cash :.2f}')
    print(f'Average CC: {total_card / cards :.2f}')

# Solution 2

expected_sum = int(input())

sold_cash = 0
sold_card = 0
total_cash = 0
total_card = 0
product_count = 0

while True:
    if total_cash + total_card >= expected_sum:
        print(f'Average CS: {total_cash / sold_cash:.2f}')
        print(f'Average CC: {total_card / sold_card:.2f}')
        break

    command = input()
    if command == 'End':
        print('Failed to collect required money for charity.')
        break

    price = int(command)

    product_count += 1
    is_cash_payment = product_count % 2 == 1

    if price <= 100 and is_cash_payment:
        total_cash += price
        sold_cash += 1
    elif price >= 10 and not is_cash_payment:
        total_card += price
        sold_card += 1
    else:
        print('Error in transaction!')
        continue

    print('Product sold!')


