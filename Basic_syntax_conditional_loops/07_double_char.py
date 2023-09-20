while True:

    string = input()

    if string == 'End':
        break
    elif string == 'SoftUni':
        continue

    for _ in string:
        print(_ * 2, end='')

    print()
