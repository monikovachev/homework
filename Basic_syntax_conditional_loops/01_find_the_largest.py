number = input()

number_as_string = sorted(number, reverse=True)

for d, d1 in enumerate(number_as_string):
    print(d1, end='')

