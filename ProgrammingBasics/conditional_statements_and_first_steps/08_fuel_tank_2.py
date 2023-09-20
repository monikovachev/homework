GASOLINE = 2.22
DIESEL = 2.33
GAS = 0.93

fuel_type = str(input())
quantity_fuel = float(input())
club_card = str(input())

gasoline_total = GASOLINE * quantity_fuel
diesel_total = DIESEL * quantity_fuel
gas_total = GAS * quantity_fuel

gasoline_total_card = gasoline_total - quantity_fuel * 0.18
diesel_total_card = diesel_total - quantity_fuel * 0.12
gas_total_card = gas_total - quantity_fuel * 0.08

if fuel_type == 'Gas' and club_card == 'Yes':
    if quantity_fuel > 25:
        gas_total_card = gas_total_card - gas_total_card * 0.10
        print(f'{gas_total_card:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        gas_total_card = gas_total_card - gas_total_card * 0.08
        print(f'{gas_total_card:.2f} lv.')
    else:
        print(f'{gas_total_card:.2f} lv.')
elif fuel_type == 'Gas' and club_card == 'No':
    if quantity_fuel > 25:
        gas_total = gas_total - gas_total * 0.10
        print(f'{gas_total:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        gas_total = gas_total - gas_total * 0.08
        print(f'{gas_total:.2f} lv.')
    else:
        print(f'{gas_total:.2f} lv.')


if fuel_type == 'Gasoline' and club_card == 'Yes':
    if quantity_fuel > 25:
        gasoline_total_card = gasoline_total_card - gasoline_total_card * 0.10
        print(f'{gasoline_total_card:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        gasoline_total_card = gasoline_total_card - gasoline_total_card * 0.08
        print(f'{gasoline_total_card:.2f} lv.')
    else:
        print(f'{gasoline_total_card:.2f} lv.')
elif fuel_type == 'Gasoline' and club_card == 'No':
    if quantity_fuel > 25:
        gasoline_total = gasoline_total - gasoline_total * 0.10
        print(f'{gasoline_total:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        gasoline_total = gasoline_total - gasoline_total * 0.08
        print(f'{gasoline_total:.2f} lv.')
    else:
        print(f'{gasoline_total:.2f} lv.')

if fuel_type == 'Diesel' and club_card == 'Yes':
    if quantity_fuel > 25:
        diesel_total_card = diesel_total_card - diesel_total_card * 0.10
        print(f'{diesel_total_card:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        diesel_total_card = diesel_total_card - diesel_total_card * 0.08
        print(f'{diesel_total_card:.2f} lv.')
    else:
        print(f'{diesel_total_card:.2f} lv.')
elif fuel_type == 'Diesel' and club_card == 'No':
    if quantity_fuel > 25:
        diesel_total = diesel_total - diesel_total * 0.10
        print(f'{diesel_total:.2f} lv.')
    elif 20 < quantity_fuel <= 25:
        diesel_total = diesel_total - diesel_total * 0.08
        print(f'{diesel_total:.2f} lv.')
    else:
        print(f'{diesel_total:.2f} lv.')






