divisor = int(input())
boundary = int(input())

for N in range(boundary, divisor - 1, -1):

    if N % divisor == 0:
        print(N)
        break

