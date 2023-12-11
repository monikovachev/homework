import re

line = input()

while line:
    pattern = r'(?i)www\.[a-z-\d+]+\.[\.a-z]+'
    links = re.findall(pattern,line)
    for link in links:
        print(link)
    line = input()
