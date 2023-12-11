import re

string = input()

pattern = r'\b(?<=\s)[A-Za-z0-9]+[\_|\-|\.]*[A-Za-z0-9]+@[a-zA-Z-]+\.?[A-Za-z]+\.{1}[A-Za-z]+\b'
match = re.findall(pattern, string)
print(*match,sep='\n')

