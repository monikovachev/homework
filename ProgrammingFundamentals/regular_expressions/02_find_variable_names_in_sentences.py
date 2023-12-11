import re

string = input()

pattern = r'\b_([a-z|A-Z|0-9]+)\b'

result = re.findall(pattern, string)

print(*result, sep=',')
