floors_total = int(input())
rooms_per_floor = int(input())

for floor in range(floors_total, 0, -1):
    for room in range(rooms_per_floor):
        if floor == floors_total:
            print(f'L{floor}{room}', end=' ')
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=' ')
        else:
            print(f'A{floor}{room}', end=' ')
    print()