n = int(input())
left_sum = 0
right_sum = 0

for numbers in range(2 * n):
    current_number = int(input())
    if numbers < n:
        left_sum += current_number
    else:
        right_sum += current_number

if right_sum == left_sum:
    print(f'Yes, sum = {left_sum}')
else:
    print(f'No, diff = {abs(left_sum - right_sum)}')
