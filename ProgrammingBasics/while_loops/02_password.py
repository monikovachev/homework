username = input()
password = input()
entry = input()

while password != entry:
    entry = input()

print(f'Welcome {username}!')
