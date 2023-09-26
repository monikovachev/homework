key = int(input())
n = int(input())
message = ''
for _ in range(n):
    letter = input()
    character = ord(letter) + key
    message += chr(character)

print(message)
