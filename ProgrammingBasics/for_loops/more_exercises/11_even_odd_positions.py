oddsum = 0
oddmin = 0
oddmax = 0
evensum = 0
evenmin = 0
evenmax = 0

count = int(input())

for _ in range(1, count + 1):
    number = float(input())
    if _ % 2 == 0:
        if number > evenmax:
            evenmax = number

        if _ == 2:
            evenmin = number
            evenmax = number

        if number < evenmin:
            evenmin = number

        evensum += number
    else:
        if number > oddmax:
            oddmax = number

        if _ == 1:
            oddmin = number
            oddmax = number

        if number < oddmin:
            oddmin = number

        oddsum += number

print(f'OddSum={oddsum:.2f},')
if oddmax == 0 and oddmin == 0:
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddMin={oddmin:.2f},')
    print(f'OddMax={oddmax:.2f},')
print(f'EvenSum={evensum:.2f},')
if evenmin == 0 and evenmax == 0:
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'EvenMin={evenmin:.2f},')
    print(f'EvenMax={evenmax:.2f}')
