string = input()
new_text = ''
x = 0
for index in range(len(string)):
    if x > 0 and string[index] != '>':
        x -= 1
    elif string[index] == '>':
        new_text += string[index]
        x += int(string[index + 1])
    else:
        new_text += string[index]

print(new_text)
