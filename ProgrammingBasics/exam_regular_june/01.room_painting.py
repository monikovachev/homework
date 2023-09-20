from math import ceil
from math import floor

box_paint_count = int(input())
wallpaper_count = int(input())
gloves_price = float(input())
brush_price = float(input())

box_paint_price = 21.50
wallpaper_price = 5.20
gloves_needed = ceil(0.35 * wallpaper_count)
brush_needed = floor(0.48 * box_paint_count)

total = box_paint_count * box_paint_price\
        + wallpaper_price * wallpaper_count\
        + gloves_price * gloves_needed\
        + brush_needed * brush_price

delivery = total / 15

print(f'This delivery will cost {delivery:.2f} lv.')