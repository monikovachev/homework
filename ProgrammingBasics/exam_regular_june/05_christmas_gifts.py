adult_count = 0
kids_count = 0
total_toys = 0
total_sweaters = 0

toy_price = 5
sweater_price = 15

command = input()

while command != 'Christmas':
    age = int(command)
    if age <= 16:
        kids_count += 1
        total_toys += 5
    else:
        adult_count += 1
        total_sweaters += 15

    command = input()

print(f'Number of adults: {adult_count}')
print(f'Number of kids: {kids_count}')
print(f'Money for toys: {total_toys}')
print(f'Money for sweaters: {total_sweaters}')

