given_string = input()

command = input().split()
while command[0] != 'Abracadabra':
    if command[0] == 'Abjuration':
        given_string = given_string.upper()
        print(given_string)
    elif command[0] == 'Necromancy':
        given_string = given_string.lower()
        print(given_string)
    elif command[0] == 'Illusion':
        index, letter = int(command[1]), command[2]
        if index > len(given_string) - 1:
            print('The spell was too weak.')
        else:
            given_string = given_string[:index] + letter + given_string[index + 1:]
            print('Done!')
    elif command[0] == 'Divination':
        first_substring, second_substring = command[1], command[2]
        if first_substring in given_string:
            given_string = given_string.replace(first_substring, second_substring)
            print(given_string)
        else:
            continue
    elif command[0] == 'Alteration':
        if command[1] in given_string:
            given_string = given_string.replace(command[1], '')
            print(given_string)
        else:
            continue
    else:
        print('The spell did not work!')

    command = input().split()


