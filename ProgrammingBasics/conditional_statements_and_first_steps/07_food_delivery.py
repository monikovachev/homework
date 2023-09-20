CHIKEN_MENU = 10.35
FISH_MENU = 12.40
VEGETERIAN_MENU = 8.15
DELIVERY_PRICE = 2.50

total_chicken = int(input())
total_fish = int(input())
total_vegeterian = int(input())

total_menu = CHIKEN_MENU * total_chicken\
             + FISH_MENU * total_fish\
             + VEGETERIAN_MENU * total_vegeterian

dessert = total_menu * 0.20

total_order = total_menu + dessert + DELIVERY_PRICE

print(total_order)

