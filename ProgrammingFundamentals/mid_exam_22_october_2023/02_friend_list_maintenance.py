friends = input().split(', ')
count_blacklist = 0
count_lost = 0

while True:
    command = input().split()
    if command[0] == 'Report':
        print(f'Blacklisted names: {count_blacklist}\nLost names: {count_lost}')
        print(*friends)
        break

    if command[0] == 'Blacklist':
        if command[1] in friends:
            index = friends.index(command[1])
            friends[index] = 'Blacklisted'
            count_blacklist += 1
            print(f'{command[1]} was blacklisted.')
        else:
            print(f'{command[1]} was not found.')

    if command[0] == 'Error':
        index = int(command[1])
        if len(friends) - 1 >= index >= 0:
            if friends[index] != 'Blacklisted' and friends[index] != 'Lost':
                print(f'{friends[index]} was lost due to an error.')
                count_lost += 1
                friends[index] = 'Lost'
        else:
            continue

    if command[0] == 'Change':
        index = int(command[1])
        if len(friends) - 1 >= index >= 0:
            print(f'{friends[index]} changed his username to {command[2]}.')
            friends[index] = command[2]
        else:
            continue

