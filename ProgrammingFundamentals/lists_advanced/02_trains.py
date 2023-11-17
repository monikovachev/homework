number_of_wagons = int(input())
train_list = [0] * number_of_wagons

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'add':
        train_list[-1] += int(command[1])

    elif command[0] == 'insert':
        index = int(command[1])
        number = int(command[2])
        train_list[index] += number

    elif command[0] == 'leave':
        index = int(command[1])
        number = int(command[2])
        train_list[index] -= number

print(train_list)




