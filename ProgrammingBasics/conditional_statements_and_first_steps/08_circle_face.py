import math

r = float(input())

circle_face = math.pi * (r ** 2)
circle_perimeter = 2 * math.pi * r

print(f'{circle_face:.2f}')
print(f'{circle_perimeter:.2f}')