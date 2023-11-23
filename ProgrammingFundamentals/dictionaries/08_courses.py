courses_dict = {}
command = input().split(' : ')
while command[0] != 'end':
    course, name = command
    if course not in courses_dict.keys():
        courses_dict[course] = []
        courses_dict[course].append(name)
    else:
        courses_dict[course].append(name)
    command = input().split(' : ')

for course, student in courses_dict.items():
    print(f'{course}: {len(courses_dict[course])}')
    for name in courses_dict[course]:
        print(f'-- {name}')
