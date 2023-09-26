budget = float(input())
flour_per_kg = float(input())
eggs_pack = flour_per_kg * 0.75
liter_milk = flour_per_kg * 1.25
bread_price = eggs_pack + flour_per_kg + liter_milk * 0.25
loaves_count = 0
colored_eggs = 0

while True:
    if bread_price >= budget:
        break

    loaves_count += 1
    colored_eggs += 3
    budget -= bread_price

    if loaves_count % 3 == 0:
        colored_eggs -= loaves_count - 2

print(f'You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')


