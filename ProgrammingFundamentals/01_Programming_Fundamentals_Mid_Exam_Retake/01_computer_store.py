total_price = 0
total_taxes = 0
is_positive = True

while True:
    command = input()
    price_including_tax = total_price + total_taxes

    if command == 'special':
        price_including_tax *= 0.9
        break
    elif command == 'regular':
        break

    price = float(command)

    if price < 0:
        print('Invalid price!')
        continue

    total_taxes += price * 0.2
    total_price += price


if total_price == 0:
    print('Invalid order!')
    is_positive = False

if is_positive:
    print(f'Congratulations you\'ve just bought a new computer!\nPrice without taxes: {total_price:.2f}$\nTaxes: {total_taxes:.2f}$')
    print(f'-----------\nTotal price: {price_including_tax:.2f}$')

