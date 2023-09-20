coffees = 0

while True:
    command = input()

    if command == 'END':
        break

    if command.lower() == 'dog' \
            or command.lower() == 'cat' \
            or command.lower() == 'coding' \
            or command.lower() == 'movie':

        if command.isupper():
            coffees += 2
        else:
            coffees += 1
    else:
        continue


if coffees > 5:
    print('You need extra sleep')
else:
    print(coffees)
