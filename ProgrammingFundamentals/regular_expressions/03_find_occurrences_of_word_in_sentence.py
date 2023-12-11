import re

string = input()
word = input()

pattern = r'\b' + word + r'\b'
match = re.findall(pattern, string, re.IGNORECASE)
print(len(match))