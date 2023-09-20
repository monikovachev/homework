VIP = 499.99
NORMAL = 249.99

budget = float(input())
ticket_type = input()
group_total = int(input())

if 1 <= group_total <= 4:
    transport_cost = budget * 0.75
elif 5 <= group_total <= 9:
    transport_cost = budget * 0.60
elif 10 <= group_total <= 24:
    transport_cost = budget * 0.50
elif 25 <= group_total <= 49:
    transport_cost = budget * 0.40
else:
    transport_cost = budget * 0.25

tickets_budget = budget - transport_cost

if ticket_type == 'VIP' and tickets_budget >= group_total * VIP:
    print(f'Yes! You have {tickets_budget - (group_total * VIP):.2f} leva left.')
elif ticket_type == 'VIP' and tickets_budget < group_total * VIP:
    print(f'Not enough money! You need {(group_total * VIP) - tickets_budget:.2f} leva.')

if ticket_type == 'Normal' and tickets_budget >= group_total * NORMAL:
    print(f'Yes! You have {tickets_budget - (group_total * NORMAL):.2f} leva left.')
elif ticket_type == 'Normal' and tickets_budget < group_total * NORMAL:
    print(f'Not enough money! You need {(group_total * NORMAL) - tickets_budget:.2f} leva.')