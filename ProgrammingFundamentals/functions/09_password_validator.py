def password_validator(string):

    list_of_errors = []

    if len(string) < 6 or len(string) > 10:
        list_of_errors.append('Password must be between 6 and 10 characters')

    if not string.isalnum():
        list_of_errors.append('Password must consist only of letters and digits')

    digit_counter = 0
    for char in string:
        if char.isdigit():
            digit_counter += 1

    if digit_counter < 2:
        list_of_errors.append('Password must have at least 2 digits')

    return list_of_errors


password = input()
errors_in_password = password_validator(password)

if not errors_in_password:
    print('Password is valid')
else:
    print('\n'.join(errors_in_password))


