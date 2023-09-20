width = int(input())
length = int(input())
height = int(input())

total_space = width * length * height
box_total = 0
is_left = False

while total_space > box_total:
    box_current = input()
    if box_current == 'Done':
        if total_space > box_total:
            is_left = True
            break

    box_total += int(box_current)

if is_left:
    print(f'{total_space - box_total} Cubic meters left.')
else:
    print(f'No more free space! You need {box_total - total_space} Cubic meters more.')
