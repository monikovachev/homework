count = int(input())
first_sum = int(input()) + int(input())
maxdiff = 0

for i in range(count - 1):
    current_sum = int(input()) + int(input())

    if abs(first_sum - current_sum) > maxdiff:
        maxdiff = abs(first_sum - current_sum)

    first_sum = current_sum

if maxdiff == 0:
    print(f'Yes, value={first_sum}')
else:
    print(f'No, maxdiff={maxdiff}')

