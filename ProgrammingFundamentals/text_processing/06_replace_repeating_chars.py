text = input()
new_text = ''
last_added = ''
for char in text:
    if char != last_added:
        new_text += char
        last_added = char

print(new_text)
