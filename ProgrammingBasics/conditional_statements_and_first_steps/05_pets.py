import math
days_gone = int(input())
food_left_kg = int(input())
daily_food_dog = float(input())
daily_food_cat = float(input())
daily_food_turtle = float(input()) / 1000

total_consumed_food = (daily_food_cat +
                       daily_food_turtle +
                       daily_food_dog) * days_gone

leftover = abs(total_consumed_food - food_left_kg)

if food_left_kg > total_consumed_food:
    print(f'{math.floor(leftover)} kilos of food left.')
else:
    print(f'{math.ceil(leftover)} more kilos of food are needed.')