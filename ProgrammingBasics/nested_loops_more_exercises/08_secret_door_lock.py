hundreds_top = int(input())
tens_top = int(input())
ones_top = int(input())
list = [2, 3, 5, 7]

for ones in range(2, hundreds_top + 1):
    for tens in range(2, tens_top + 1):
        for hundreds in range(2, ones_top + 1):

            if ones % 2 == 0 \
                    and hundreds % 2 == 0 \
                    and tens in list:
                print(f'{ones} {tens} {hundreds}')

