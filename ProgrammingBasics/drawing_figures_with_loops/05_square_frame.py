n = int(input())
tire = '- '
print(f'+ {(n - 2) * tire}+')

for middle in range(n - 2):
    print(f'| {(n - 2) * tire}|')

print(f'+ {(n - 2) * tire}+')




