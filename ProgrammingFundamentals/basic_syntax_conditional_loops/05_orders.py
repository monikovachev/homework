orders_total = int(input())
total_price = 0

for order in range(orders_total):

    capsule_price = float(input())
    days = int(input())
    needed_capsules_daily = int(input())

    if not 0.01 <= capsule_price <= 100 \
            or not 1 <= days <= 31 \
            or not 1 <= needed_capsules_daily <= 2000:
        continue

    price = capsule_price * needed_capsules_daily * days

    print(f'The price for the coffee is: ${price:.2f}')

    total_price += price

print(f'Total: ${total_price:.2f}')
