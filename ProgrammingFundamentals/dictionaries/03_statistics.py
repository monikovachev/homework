products_input = input().split(': ')
products_dict = {}

while products_input[0] != 'statistics':

    product = products_input[0]
    quantity = int(products_input[1])
    if product in products_dict:
        products_dict[product] += quantity
    else:
        products_dict[product] = quantity
    products_input = input().split(': ')

print(f'Products in stock:')
for product, quantity in products_dict.items():
    print(f'- {product}: {quantity}')
print(f'Total Products: {len(products_dict)}')
print(f'Total Quantity: {sum(products_dict.values())}')

