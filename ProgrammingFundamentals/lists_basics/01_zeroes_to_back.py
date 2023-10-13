given_string = input().split(', ')
numbers = []

for _ in given_string:
    numbers.append(int(_))
found = numbers.count(0)

while 0 in numbers:
    numbers.remove(0)

for _ in range(found):
    numbers.append(0)

print(numbers)
