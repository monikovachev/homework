order_joinery = int(input())
type_joinery = input()
delivery = input()

price = 0
discount = 1
additional_discount = 1
transport = 0
if delivery == 'With delivery':
    transport = 60

if order_joinery > 99:
    additional_discount = 0.96
elif order_joinery < 10:
    print(f'Invalid order')

if type_joinery == '90X130':
    price = 110
    if order_joinery > 60:
        discount = 0.92
    elif order_joinery > 30:
        discount = 0.95
elif type_joinery == '100X150':
    price = 140
    if order_joinery > 80:
        discount = 0.90
    elif order_joinery > 40:
        discount = 0.94
elif type_joinery == '130X180':
    price = 190
    if order_joinery > 50:
        discount = 0.88
    elif order_joinery > 20:
        discount = 0.93
else:
    price = 250
    if order_joinery > 50:
        discount = 0.86
    elif order_joinery > 25:
        discount = 0.91

total = (((order_joinery * price) * discount) + transport) * additional_discount

if order_joinery >= 10:
    print(f'{total:.2f} BGN')

