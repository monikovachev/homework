gifts_string = input().split()
command = input().split()
while not command[0] == 'No' and not command[1] == 'Money':

    if command[0] == 'OutOfStock':
        while command[1] in gifts_string:
            index = gifts_string.index(command[1])
            gifts_string[index] = 'None'

    elif command[0] == 'Required':
        index = int(command[2])
        if len(gifts_string) > index > 0:
            gifts_string[index] = command[1]

    elif command[0] == 'JustInCase':
        gifts_string.pop()
        gifts_string.append(command[1])

    command = input().split()

while 'None' in gifts_string:
    gifts_string.remove('None')

print(*gifts_string, sep=' ')
