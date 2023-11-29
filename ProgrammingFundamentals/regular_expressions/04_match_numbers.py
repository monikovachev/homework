import re

numbers = input()

regex_pattern = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
matches = re.finditer(regex_pattern, numbers)

for match in matches:
    print(match.group(), end=' ')
