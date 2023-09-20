total = 0
command = input()

while command != 'NoMoreMoney':
    number = float(command)
    if number < 0:
        print(f'Invalid operation!')
        break
    print(f'Increase: {number:.2f}')
    total += number
    command = input()

print(f'Total: {total:.2f}')
