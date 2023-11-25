usernames = input().split(', ')
for user in usernames:
    is_valid = True

    if not 3 <= len(user) <= 16:
        is_valid = False
    for char in user:
        if not (char.isalnum()
                or char == '-'
                or char == '_'):
            is_valid = False
    if ' ' in user:
        is_valid = False

    if is_valid:
        print(f'{user}')
