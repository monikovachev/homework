numbers_string = input().split()
numbers_list = []

for number in numbers_string:
    numbers_list.append(abs(float(number)))

print(numbers_list)
