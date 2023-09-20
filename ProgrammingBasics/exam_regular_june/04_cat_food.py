price_gram = 12.45 / 1000
cats_count = int(input())
group1 = 0
group2 = 0
group3 = 0
total = 0

for _ in range(cats_count):
    grams_per_day = float(input())
    if 100 <= grams_per_day < 200:
        group1 += 1
    elif 200 <= grams_per_day < 300:
        group2 += 1
    elif 300 <= grams_per_day < 400:
        group3 += 1
    total += grams_per_day

price = total * price_gram
print(f'Group 1: {group1} cats.')
print(f'Group 2: {group2} cats.')
print(f'Group 3: {group3} cats.')
print(f'Price for food per day: {price:.2f} lv.')
