count = int(input())

result = 0
invalid_numbers = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0
group5 = 0

for _ in range(count):
    number = int(input())
    if 0 <= number <= 9:
        result += number * 0.20
        group1 += 1
    elif 10 <= number <= 19:
        result += number * 0.30
        group2 += 1
    elif 20 <= number <= 29:
        result += number * 0.40
        group3 += 1
    elif 30 <= number <= 39:
        result += 50
        group4 += 1
    elif 40 <= number <= 50:
        result += 100
        group5 += 1
    else:
        invalid_numbers += 1
        result /= 2

print(f'{result :.2f}')
print(f'From 0 to 9: {group1 / count * 100 :.2f}%')
print(f'From 10 to 19: {group2 / count * 100 :.2f}%')
print(f'From 20 to 29: {group3 / count * 100 :.2f}%')
print(f'From 30 to 39: {group4 / count * 100 :.2f}%')
print(f'From 40 to 50: {group5 / count * 100 :.2f}%')
print(f'Invalid numbers: {invalid_numbers / count * 100 :.2f}%')
