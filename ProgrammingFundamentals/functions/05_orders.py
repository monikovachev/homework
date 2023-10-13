def order_price(product, quantity):
    if product == 'coffee':
        price = 1.50
    elif product == 'water':
        price = 1
    elif product == 'coke':
        price = 1.40
    elif product == 'snacks':
        price = 2

    result = f'{(price * quantity):.2f}'
    return result


product = input()
quantity = int(input())
order = order_price(product, quantity)
print(order)
