employees_happiness = list(map(int, input().split()))
happiness_improvement_factor = int(input())

happiness_with_factor = list(map(lambda number: number * happiness_improvement_factor, employees_happiness))
average_happiness = sum(happiness_with_factor) / len(happiness_with_factor)

filtered = list(filter(lambda x: x >= average_happiness, happiness_with_factor))

if len(filtered) >= len(happiness_with_factor) / 2:
    print(f'Score: {len(filtered)}/{len(happiness_with_factor)}. Employees are happy!')
else:
    print(f'Score: {len(filtered)}/{len(happiness_with_factor)}. Employees are not happy!')
