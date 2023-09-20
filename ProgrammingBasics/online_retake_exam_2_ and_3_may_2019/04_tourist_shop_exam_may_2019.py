counter = 1
total = 0
budget = float(input())
command = input()

while not command == 'Stop':
    price_product = float(input())
    if counter % 3 == 0:
        price_product *= 0.5
    total += price_product
    if budget < price_product:
        print(f'You don\'t have enough money!\nYou need {price_product - budget:.2f} leva!')
        break

    budget -= price_product
    command = input()
    counter += 1

if command == 'Stop':
    print(f'You bought {counter - 1} products for {total:.2f} leva.')
