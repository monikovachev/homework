gas_type = str(input())
liters = float(input())

if gas_type == 'Gas' or gas_type == 'Diesel' or gas_type == 'Gasoline':
    if liters >= 25:
        print(f'You have enough {str.lower(gas_type)}.')

if gas_type == 'Gas' or gas_type == 'Diesel' or gas_type == 'Gasoline':
    if liters < 25:
        print(f'Fill your tank with {str.lower(gas_type)}!')
else:
    print(f'Invalid fuel!')