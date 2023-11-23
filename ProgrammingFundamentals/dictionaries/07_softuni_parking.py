parking_info = {}

number_of_commands = int(input())

for info in range(number_of_commands):
    command = input().split()

    if command[0] == 'register':
        user, license_plate = command[1], command[2]
        if user not in parking_info.keys():
            parking_info[user] = license_plate
            print(f'{user} registered {parking_info[user]} successfully')
        else:
            if license_plate == parking_info[user]:
                print(f'ERROR: already registered with plate number {parking_info[user]}')
    elif command[0] == 'unregister':
        user = command[1]
        if user not in parking_info.keys():
            print(f'ERROR: user {user} not found')
        else:
            del parking_info[user]
            print(f'{user} unregistered successfully')

for user, license in parking_info.items():
    print(f'{user} => {license}')
