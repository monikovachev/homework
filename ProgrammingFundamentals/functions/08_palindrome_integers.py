def is_palindrome(integers):
    for number in integers:
        if number[::-1] == number:
            print(True)
        else:
            print(False)


given_integers = input().split(', ')
is_palindrome(given_integers)

