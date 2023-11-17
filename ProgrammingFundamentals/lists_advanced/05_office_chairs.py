rooms = int(input())
free_chairs = 0
game_on = True
for room in range(1, rooms + 1):

    command = input().split()

    chairs = len(command[0])
    visitors = int(command[1])

    if chairs - visitors > 0:
        free_chairs += chairs - visitors

    if visitors > chairs:
        game_on = False
        print(f'{visitors - chairs} more chairs needed in room {room}')

if game_on:
    print(f'Game On, {free_chairs} free chairs left')
