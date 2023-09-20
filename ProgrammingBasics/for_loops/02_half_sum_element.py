import sys

count = int(input())
max_number = -sys.maxsize
num_sum = 0

for numbers in range(count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    num_sum += current_number

rest_sum = num_sum - max_number
if rest_sum == max_number:
    print(f'Yes\nSum = {max_number}')
else:
    print(f'No\nDiff = {abs(max_number - rest_sum)}')





