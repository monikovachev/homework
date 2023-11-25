text = input()
encrypted_text = ''
for char in text:
    char = ord(char) + 3
    encrypted_text += chr(char)

print(encrypted_text)