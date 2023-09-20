NYLON_PRICE = 1.50
PAINT_PRICE = 14.50
PAINT_THINNER_PRICE = 5
BAG = 0.40


nylon_total = int(input())
paint_total = int(input())
paint_thinner_total = int(input())
work_hours = int(input())

extra_safe = 0.10 * (PAINT_PRICE * paint_total) +\
             2 * NYLON_PRICE\
             + BAG

total_materials = NYLON_PRICE * nylon_total\
                  + PAINT_PRICE * paint_total\
                  + PAINT_THINNER_PRICE * paint_thinner_total + extra_safe

work_pay = work_hours * (total_materials * 0.30)

print(total_materials + work_pay)


