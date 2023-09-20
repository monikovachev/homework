age = int(input())
machine_price = float(input())
toy_price = int(input())

money = 0
toys_count = 0

for _ in range(1, age + 1):
    current_age = _
    if current_age % 2 == 0:
        money += 10 * _ / 2
    else:
        toys_count += 1

brother_tax = age // 2

total_money = (money + (toys_count * toy_price)) - brother_tax

if total_money >= machine_price:
    print(f'Yes! {total_money - machine_price:.2f}')
else:
    print(f'No! {machine_price - total_money:.2f}')
