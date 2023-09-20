kg_veggies_price = float(input())
kg_fruits_price = float(input())
total_kg_veggies = int(input())
total_kg_fruits = int(input())

revenue = kg_veggies_price * total_kg_veggies + kg_fruits_price * total_kg_fruits
revenue_eur = revenue / 1.94

print(f'{revenue_eur:.2f}')

