months_count = int(input())

elec_bill = 0
water_bill = 20
net_bill = 15
elec_total = 0
other_total = 0

for _ in range(months_count):
    elec_bill = float(input())
    other_bill = (35 + elec_bill) * 1.20
    elec_total += elec_bill
    other_total += other_bill

all = (water_bill * months_count) + (net_bill * months_count) + elec_total + other_total

print(f'Electricity: {elec_total:.2f} lv')
print(f'Water: {water_bill * months_count:.2f} lv')
print(f'Internet: {net_bill * months_count:.2f} lv')
print(f'Other: {other_total:.2f} lv')
print(f'Average: {all / months_count:.2f} lv')
