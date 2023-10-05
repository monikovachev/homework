given_integers = input().split()
n = int(input())
numbers = []

for num in given_integers:
    numbers.append(int(num))

for _ in range(n):
    numbers.remove(min(numbers))

print(*numbers, sep=', ')

# numbers = list(map(int, input().split()))
# remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
#
# print(*numbers, sep=', ')
