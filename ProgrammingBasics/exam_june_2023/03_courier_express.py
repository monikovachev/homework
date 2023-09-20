weight_order_kg = float(input())
type_shipping = input()
distance_kms = int(input())
price_per_km = 0        #in leva
tax = 0
if type_shipping == 'standard':
    if weight_order_kg < 1:
       price_per_km = 0.03
    elif weight_order_kg < 10:
        price_per_km = 0.05
    elif weight_order_kg < 40:
        price_per_km = 0.10
    elif weight_order_kg < 90:
        price_per_km = 0.15
    elif weight_order_kg < 150:
        price_per_km = 0.20
    total = distance_kms * price_per_km
elif type_shipping == 'express':
    if weight_order_kg < 1:
       price_per_km = 0.03
       tax = price_per_km * 0.80
    elif weight_order_kg < 10:
        price_per_km = 0.05
        tax = price_per_km * 0.40
    elif weight_order_kg < 40:
        price_per_km = 0.10
        tax = price_per_km * 0.05
    elif weight_order_kg < 90:
        price_per_km = 0.15
        tax = price_per_km * 0.02
    elif weight_order_kg < 150:
        price_per_km = 0.20
        tax = price_per_km * 0.01
    total = distance_kms * price_per_km + ((tax * weight_order_kg) * distance_kms)


print(f'The delivery of your shipment with weight of {weight_order_kg:.3f} kg. would cost {total:.2f} lv.')

