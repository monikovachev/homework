numbers_given = input().split()
numbers_as_digits = []

for num in numbers_given:
    numbers_as_digits.append(int(num))

is_even = lambda number: number % 2 == 0

even_list = list(filter(is_even, numbers_as_digits))
print(even_list)
