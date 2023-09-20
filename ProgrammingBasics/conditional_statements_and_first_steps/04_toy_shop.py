PUZZLE_PRICE = 2.60
DOLL_PRICE = 3
BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2

vacation_price = float(input())
puzzle_quantity = int(input())
doll_quantity = int(input())
bear_quantity = int(input())
minion_quantity = int(input())
truck_quantity = int(input())

total_order = PUZZLE_PRICE * puzzle_quantity \
              + DOLL_PRICE * doll_quantity \
              + BEAR_PRICE * bear_quantity \
              + MINION_PRICE * minion_quantity \
              + TRUCK_PRICE * truck_quantity

if puzzle_quantity + doll_quantity + bear_quantity + minion_quantity + truck_quantity >= 50:
    total_order = total_order - total_order * 0.25

revenue = total_order - total_order * 0.10
leftover = revenue - vacation_price

if leftover < 0:
    leftover = leftover * -1

if vacation_price <= revenue:
    print(f'Yes! {leftover:.2f} lv left.')
else:
    print(f'Not enough money! {leftover:.2f} lv needed.')