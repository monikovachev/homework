type_flower = input()
quantity_flowers = int(input())
budget = int(input())

ROSE_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

flower_price = 0

if type_flower == 'Roses':
    flower_price = ROSE_PRICE
    if quantity_flowers > 80:
        flower_price = ROSE_PRICE * 0.90

elif type_flower == 'Dahlias':
    flower_price = DAHLIAS_PRICE
    if quantity_flowers > 90:
        flower_price = DAHLIAS_PRICE * 0.85

elif type_flower == 'Tulips':
    flower_price = TULIPS_PRICE
    if quantity_flowers > 80:
        flower_price = TULIPS_PRICE * 0.85

elif type_flower == 'Narcissus':
    flower_price = NARCISSUS_PRICE
    if quantity_flowers < 120:
        flower_price = NARCISSUS_PRICE * 1.15

elif type_flower == 'Gladiolus':
    flower_price = GLADIOLUS_PRICE
    if quantity_flowers < 80:
        flower_price = GLADIOLUS_PRICE * 1.20

total_price = flower_price * quantity_flowers
leftover = abs(budget - total_price)

if budget >= total_price:
    print(f'Hey, you have a great garden with {quantity_flowers} {type_flower} and {leftover:.02f} leva left.')
else:
    print(f'Not enough money, you need {leftover:.2f} leva more.')
