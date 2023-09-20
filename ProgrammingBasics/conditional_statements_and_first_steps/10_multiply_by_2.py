import sys

for _ in range(sys.maxsize):
    number = float(input())
    if number < 0:
        print(f'Negative number!')
        break
    else:
        print(f'Result: {number * 2 :.2f}')




