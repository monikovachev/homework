import re

pattern = '>{2}([a-zA-Z]+)<{2}(\\d+|\\d+\\.\\d+)!(\\d+)'
total_cost = 0
products_list = []
while True:
    command = input()
    if command == 'Purchase':
        break
    products = re.search(pattern, command)
    if products:
        products_list.append(products.group(1))
        total_cost += float(products.group(2)) * int(products.group(3))

print('Bought furniture:')
for product in products_list:
    print(product)
print(f'Total money spend: {total_cost:.2f}')

