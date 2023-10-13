def min_max_and_sum(string):
    ascended_list = []

    for char in string:
        ascended_list.append(int(char))

    return f'The minimum number is {min(ascended_list)}\nThe maximum number is {max(ascended_list)}\nThe sum number is: {sum(ascended_list)}'


numbers_as_string = input().split()
print(min_max_and_sum(numbers_as_string))
