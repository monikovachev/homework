company_dict = {}
command = input().split(' -> ')
while command[0] != 'End':
    company, employee_id = command
    if company not in company_dict.keys():
        company_dict[company] = []

    if employee_id not in company_dict[company]:
        company_dict[company].append(employee_id)

    command = input().split(' -> ')

for company, employee in company_dict.items():
    print(f'{company}')
    for id in company_dict[company]:
        print(f'-- {id}')

