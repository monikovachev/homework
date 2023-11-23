inventory = {'shards': 0, 'fragments': 0, 'motes': 0}
current_items = input().split()
obtained = False

while not obtained:
    for index in range(0, len(current_items), 2):
        value = int(current_items[index])
        key = current_items[index + 1].lower()
        if key not in inventory.keys():
            inventory[key] = 0
        inventory[key] += value

        if inventory['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            inventory['shards'] -= 250
            obtained = True
        elif inventory['fragments'] >= 250:
            print(f'Valanyr obtained!')
            inventory['fragments'] -= 250
            obtained = True
        elif inventory['motes'] >= 250:
            print(f'Dragonwrath obtained!')
            inventory['motes'] -= 250
            obtained = True

        if obtained:
            break
    if obtained:
        break

    current_items = input().split()


for material, quantity in inventory.items():
    print(f'{material}: {quantity}')