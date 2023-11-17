first_string = input().split(', ')
second_string = input().split(', ')
final_list = []
for string in first_string:
    for string_one in second_string:
        if string in string_one:
            final_list.append(string)
            break

print(final_list)
