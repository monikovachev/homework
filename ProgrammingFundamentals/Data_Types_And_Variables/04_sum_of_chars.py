N = int(input())
total = 0
for _ in range(N):

    letter = input()
    total += ord(letter)

print(f'The sum equals: {total}')
