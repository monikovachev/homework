money = float(input())
year_death = int(input())

money_spent = 0

for _ in range(1800, year_death + 1):
    if _ % 2 == 0:
        money_spent += 12000
    else:
        money_spent += 12000 + 50 * (18 + (_ - 1800))

diff = abs(money - money_spent)

if money >= money_spent:
    print(f'Yes! He will live a carefree life and will have {diff:.2f} dollars left.')
else:
    print(f'He will need {diff:.2f} dollars to survive.')
