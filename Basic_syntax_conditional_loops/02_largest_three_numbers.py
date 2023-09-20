first = int(input())
second = int(input())
third = int(input())

largest = first

if largest < second:
    largest = second

if largest < third:
    largest = third

print(largest)

