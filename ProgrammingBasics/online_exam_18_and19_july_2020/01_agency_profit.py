company_name = input()
adult_ticket_count = int(input())
kids_ticket_count = int(input())
price_adult = float(input())
tax = float(input())

price_kids = price_adult * 0.30 + tax
price_adult += tax

profit = (adult_ticket_count * price_adult +
          kids_ticket_count * price_kids) * 0.20

print(f'The profit of your agency from {company_name} tickets is {profit :.2f} lv.')
