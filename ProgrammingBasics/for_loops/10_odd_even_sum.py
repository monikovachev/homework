n = int(input())
even_sum = 0
odd_sum = 0

for _ in range(n):
    current_number = int(input())
    if _ % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if even_sum == odd_sum:
    print(f'Yes\nSum = {even_sum}')
else:
    print(f'No\nDiff = {abs(even_sum - odd_sum)}')

