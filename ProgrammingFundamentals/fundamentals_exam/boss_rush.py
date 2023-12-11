import re
n = int(input())

pattern = r'\|([A-Z]{4,})\|:#([a-zA-Z]+\s{1}[A-Za-z]+)#'

for check in range(n):
    given_command = input()
    result = re.search(pattern, given_command)
    if result:
        print(rf'{result.group(1)}, The {result.group(2)}')
        print(rf'>> Strength: {len(result.group(1))}')
        print(rf'>> Armor: {len(result.group(2))}')
    else:
        print('Access denied!')

