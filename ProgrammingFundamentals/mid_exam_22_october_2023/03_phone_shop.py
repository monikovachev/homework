phones = input().split(', ')

while True:
    command = input().split(' - ')
    if command[0] == 'End':
        print(', '.join(phones))
        break

    elif command[0] == 'Add':
        if command[1] in phones:
            continue
        else:
            phones.append(command[1])

    elif command[0] == 'Remove':
        if command[1] in phones:
            phones.remove(command[1])
        else:
            continue

    elif command[0] == 'Bonus phone':
        old_new_phone = command[1].split(':')
        if old_new_phone[0] in phones:
            index = phones.index(old_new_phone[0])
            phones.insert(index + 1, old_new_phone[1])
        else:
            continue

    elif command[0] == 'Last':
        if command[1] in phones:
            phones.remove(command[1])
            phones.append(command[1])


