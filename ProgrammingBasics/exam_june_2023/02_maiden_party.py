love_poem = 0.60
wax_rose = 7.20
keyring = 3.60
caricature = 18.20
lucky_surprise = 22
discount = 1
hosting_expense = 0.10

money_needed = float(input())
count_love_poems = int(input())
count_wax_roses = int(input())
count_keyrings = int(input())
count_caricatures = int(input())
count_lucky_surprise = int(input())

total_income = love_poem * count_love_poems \
               + wax_rose * count_wax_roses \
               + keyring * count_keyrings \
               + caricature * count_caricatures \
               + lucky_surprise * count_lucky_surprise

if count_love_poems + count_wax_roses + count_keyrings + count_caricatures + count_lucky_surprise >= 25:
    discount = 0.65

total = (total_income * discount) * 0.90

if total >= money_needed:
    print(f'Yes! {total - money_needed:.2f} lv left.')
else:
    print(f'Not enough money! {money_needed - total:.2f} lv needed.')
