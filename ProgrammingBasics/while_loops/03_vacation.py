money_needed = float(input())
available_money = float(input())

days_past = 0
days_spending_consecutively = 0
has_enough = True

while available_money < money_needed:
    action = input()
    money_sum = float(input())

    if action == 'spend':
        available_money -= money_sum
        if available_money < 0:
            available_money = 0
    else:
        available_money += money_sum

    days_past += 1
    last_action = action

    if last_action == 'spend':
        days_spending_consecutively += 1
        if days_spending_consecutively >= 5:
            has_enough = False
            break
    else:
        days_spending_consecutively = 0

if has_enough:
    print(f'You saved the money for {days_past} days.')
else:
    print(f'You can\'t save the money.\n{days_past}')

