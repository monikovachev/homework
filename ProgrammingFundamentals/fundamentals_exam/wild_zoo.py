animals_food_limit = {}
animals_area = {}

while True:
    command = input().split(':')
    if command[0] == 'EndDay':
        break

    if command[0] == 'Add':
        animal_name, needed_food, living_area = command[1].split('-')
        if animal_name in animals_food_limit:
            animals_food_limit[animal_name] += int(needed_food)
        else:
            animals_food_limit[animal_name] = int(needed_food)
        if not living_area in animals_area.keys():
            animals_area[living_area] = []
        if animal_name in animals_area[living_area]:
            continue
        else:
            animals_area[living_area].append(animal_name)
    elif command[0] == 'Feed':
        animal_name, food = command[1].split('-')
        if animal_name in animals_food_limit.keys():
            animals_food_limit[animal_name] -= int(food)
            if animals_food_limit[animal_name] <= 0:
                print(f'{animal_name.lstrip()} was successfully fed')
                del animals_food_limit[animal_name]
                for area, name in animals_area.items():
                    if animal_name in name:
                        animals_area[area].remove(animal_name)
        else:
            continue

print('Animals:')
for animal, food in animals_food_limit.items():
    print(f'{animal} -> {food}g')
print('Areas with hungry animals:')
for area, animal in animals_area.items():
    if len(animals_area[area]) == 0:
        continue
    print(f' {area}: {len(animals_area[area])}')
