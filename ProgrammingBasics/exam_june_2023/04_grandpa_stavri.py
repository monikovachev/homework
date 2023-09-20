days = int(input())
liters_total = 0
degree_total = 0

for day in range(days):
    quantity_rakia = float(input())
    degree_rakia = float(input())

    degree_total += quantity_rakia * degree_rakia
    liters_total += quantity_rakia

degree_avg = degree_total / liters_total

print(f'Liter: {liters_total:.2f}')
print(f'Degrees: {degree_avg:.2f}')
if degree_avg < 38:
    print('Not good, you should baking!')
elif degree_avg <= 42:
    print('Super!')
else:
    print('Dilution with distilled water!')
