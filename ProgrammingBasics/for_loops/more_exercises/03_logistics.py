shipment_count = int(input())
tons_bus = 0
tons_tir = 0
tons_train = 0

for _ in range(shipment_count):
    tons_shipment = int(input())
    if tons_shipment <= 3:
        tons_bus += tons_shipment
    elif tons_shipment <= 11:
        tons_tir += tons_shipment
    else:
        tons_train += tons_shipment

total_tons = tons_bus + tons_tir + tons_train

avg_price_per_ton = (tons_bus * 200 + tons_tir * 175 + tons_train * 120) / total_tons

print(f'{avg_price_per_ton:.2f}')
print(f'{tons_bus / total_tons * 100 :.2f}%')
print(f'{tons_tir / total_tons * 100 :.2f}%')
print(f'{tons_train / total_tons * 100 :.2f}%')

