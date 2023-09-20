movie_type = input()
rows = int(input())
columns = int(input())

PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5.00

seats = rows * columns

if movie_type == 'Premiere':
    income = seats * PREMIERE_PRICE
elif movie_type == 'Normal':
    income = seats * NORMAL_PRICE
else:
    income = seats * DISCOUNT_PRICE

print(f'{income:.2f} leva')
