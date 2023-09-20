counter = 0
beginning = int(input())
end = int(input())
magic_number = int(input())
is_found = False

for n1 in range(beginning, end + 1):
    for n2 in range(beginning, end + 1):
        counter += 1

        if n1 + n2 == magic_number:
            is_found = True
            print(f'Combination N:{counter} ({n1} + {n2} = {magic_number})')
            break

    if is_found:
        break

if not is_found:
    print(f'{counter} combinations - neither equals {magic_number}')
