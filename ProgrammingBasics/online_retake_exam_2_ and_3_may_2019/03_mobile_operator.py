contract_length = input()
contract_type = input()
mobile_internet_extra = input()
month_payments = int(input())

if contract_type == 'Small':
    if contract_length == 'one':
        price = 9.98
    else:
        price = 8.58
elif contract_type == 'Middle':
    if contract_length == 'one':
        price = 18.99
    else:
        price = 17.09
elif contract_type == 'Large':
    if contract_length == 'one':
        price = 25.98
    else:
        price = 23.59
else:
    if contract_length == 'one':
        price = 35.99
    else:
        price = 31.79

if mobile_internet_extra == 'yes':
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

total = month_payments * price

if contract_length == 'two':
    total *= 0.9625

print(f'{total:.2f} lv.')
