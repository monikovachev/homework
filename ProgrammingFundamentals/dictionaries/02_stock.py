text = input().split()
searched_products = input().split()
stock = {}

for i in range(0, len(text), 2):
    food = text[i]
    quantity = text[i + 1]
    stock[food] = quantity

for p in range(len(searched_products)):
    product = searched_products[p]
    if product in stock.keys():
        print(f'We have {stock.get(product)} of {product} left')
    else:
        print(f'Sorry, we don\'t have {product}')



