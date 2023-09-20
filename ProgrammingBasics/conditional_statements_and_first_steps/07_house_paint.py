GREEN_DYE_PER_LITER = 3.4
RED_DYE_PER_LITER = 4.3

x = float(input())
y = float(input())
h = float(input())

front_wall = x ** 2 - 2.4
back_wall = x ** 2
side_wall = x * y - 2.25
roof_wall = x * y
roof_triangle = x * h /2

green_dye_total = (front_wall + 2 * side_wall + back_wall) / GREEN_DYE_PER_LITER
red_dye_total = (2 * roof_wall + 2 * roof_triangle) / RED_DYE_PER_LITER

print(f'{green_dye_total:.2f}')
print(f'{red_dye_total:.2f}')

