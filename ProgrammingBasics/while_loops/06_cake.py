width = int(input())
length = int(input())

total_pieces = width * length
is_left = False

while total_pieces > 0:
    taken = input()

    if taken == 'STOP':
        if total_pieces > 0:
            is_left = True
            break

    total_pieces -= int(taken)


if is_left:
    print(f'{total_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(total_pieces)} pieces more.')

