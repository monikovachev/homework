import math
MAGNOLIA = 3.25
ZUMBUL = 4
ROSE = 3.50
CACTUS = 8

magnolia_quantity = int(input())
zumbul_quantity = int(input())
rose_quantity = int(input())
cactus_quantity = int(input())
present_price = float(input())

revenue = magnolia_quantity * MAGNOLIA\
          + zumbul_quantity * ZUMBUL\
          + rose_quantity * ROSE\
          + cactus_quantity * CACTUS

total_revenue = revenue - revenue * 0.05

leftover = abs(present_price - total_revenue)

if present_price <= total_revenue:
    print(f'She is left with {math.floor(leftover)} leva.')
else:
    print(f'She will have to borrow {math.ceil(leftover)} leva.')