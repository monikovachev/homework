c_count = 0
o_count = 0
n_count = 0
the_word = ''
result_string = ''
command = input()

while command != 'End':

    if not command.isalpha():
        command = input()
        continue

    if command == 'c' and c_count == 0:
        c_count += 1
        if c_count == 1 and o_count == 1 and n_count == 1:
            result_string += f'{the_word} '
            the_word = ''
            c_count = 0
            o_count = 0
            n_count = 0
        command = input()
        continue
    elif command == 'o' and o_count == 0:
        o_count += 1
        if c_count == 1 and o_count == 1 and n_count == 1:
            result_string += f'{the_word} '
            the_word = ''
            c_count = 0
            o_count = 0
            n_count = 0
        command = input()
        continue
    elif command == 'n' and n_count == 0:
        n_count += 1
        if c_count == 1 and o_count == 1 and n_count == 1:
            result_string += f'{the_word} '
            the_word = ''
            c_count = 0
            o_count = 0
            n_count = 0
        command = input()
        continue


    the_word += command
    command = input()


print(result_string)
