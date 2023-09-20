counter = 0
magic_number = int(input())
is_found = False
fourth = ''

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                if magic_number == (a * b) + (c * d) and a < b and c > d:
                    counter += 1
                    print(f'{a}{b}{c}{d}', end=' ')

                if counter == 4:
                    fourth = f'{a}{b}{c}{d}'
                    counter += 1
                    is_found = True

if is_found:
    print(f'\nPassword: {fourth}')
else:
    print('\nNo!')

