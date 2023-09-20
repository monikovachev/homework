order = input()
order_list = order.split(', ')

for index, animal in enumerate(reversed(order_list)):

    if animal == 'wolf' and index == 0:
        print('Please go away and stop eating my sheep')
        break

    elif animal == 'wolf' and index != 0:
        print(f'Oi! Sheep number {index}! You are about to be eaten by a wolf!')
        break


