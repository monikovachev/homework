order_prices = {}
order_quantity = {}
while True:
    command = input().split()
    if 'buy' in command:
        break

    product_name, price, quantity = command[0], float(command[1]), int(command[2])

    if product_name not in order_quantity.keys():
        order_quantity[product_name] = quantity
        order_prices[product_name] = price
    else:
        order_quantity[product_name] += quantity
        if price != order_prices[product_name]:
            order_prices[product_name] = price

for product, price in order_prices.items():
    total_price = order_quantity[product] * price
    print(f'{product} -> {total_price:.2f}')



