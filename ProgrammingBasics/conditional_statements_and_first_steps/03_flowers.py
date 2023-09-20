hrizantems_quantity = int(input())
roses_quantity = int(input())
laleta_quantity = int(input())
season = input()
holiday = input()

hrizantem_price = 2
rose_price = 4.10
lale_price = 2.50
discount_1 = 1
discount_2 = 1

if (hrizantems_quantity + roses_quantity + laleta_quantity) > 20:
    discount_2 = 0.80

if season == 'Spring' or season == 'Summer':
    if holiday == 'Y':
        hrizantem_price *= 1.15
        rose_price *= 1.15
        lale_price *= 1.15
    if laleta_quantity > 7:
        discount_1 = 0.95
elif season == 'Autumn' or season == 'Winter':
    hrizantem_price = 3.75
    rose_price = 4.50
    lale_price = 4.15
    if holiday == 'Y':
        hrizantem_price *= 1.15
        rose_price *= 1.15
        lale_price *= 1.15
    if roses_quantity >= 10 and season == 'Winter':
        discount_1 = 0.90

flower_total = (hrizantems_quantity * hrizantem_price)\
        + (roses_quantity * rose_price)\
        + (laleta_quantity * lale_price)

total = (flower_total * discount_1) * discount_2 + 2
print(f'{total:.2f}')





