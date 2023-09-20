import math
from math import pi


figure_type = input()

if figure_type == 'square':
    square_length = float(input())
    print(f'{square_length ** 2:.3f}')

elif figure_type == 'rectangle':
    rectangle_length = float(input())
    rectangle_width = float(input())
    print(f'{rectangle_length * rectangle_width:.3f}')

elif figure_type == 'circle':
    radius_circle = float(input())
    print(f'{math.pi * (radius_circle ** 2):.3f}')

elif figure_type == 'triangle':
    triangle_length = float(input())
    triangle_height = float(input())
    print(f'{(triangle_height * triangle_length) / 2:.3f}')



