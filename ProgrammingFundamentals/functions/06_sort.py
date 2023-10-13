def ascend_numbers(string):
    ascended_list = []

    for char in string:
        ascended_list.append(int(char))

    return sorted(ascended_list)


integers_as_string = input().split()
result = ascend_numbers(integers_as_string)
print(result)
