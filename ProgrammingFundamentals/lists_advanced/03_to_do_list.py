def to_do_list_sort():
    to_do_list = []
    while True:
        command = input()

        if command == 'End':
            break

        to_do_list.append(command)

    sorted_list = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
    return [x.split('-')[1] for x in sorted_list]


result = to_do_list_sort()
print(result)