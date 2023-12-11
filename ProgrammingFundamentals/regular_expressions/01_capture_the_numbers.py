import re

line = input()
while line:
    number = re.findall(r'\d+', line)
    if number:
        print(' '.join(number), end=' ')
    line = input()
