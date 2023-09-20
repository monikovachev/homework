failed_number = int(input())
total_grade = 0
poor_grades = 0
name_problem = ''
solved_problems = 0
has_failed = True

while poor_grades < failed_number:
    name_problem = input()
    if name_problem == 'Enough':
        has_failed = False
        break

    current_grade = int(input())
    if current_grade <= 4:
        poor_grades += 1

    total_grade += current_grade
    solved_problems += 1
    last_problem = name_problem

if has_failed:
    print(f'You need a break, {failed_number} poor grades.')
else:
    print(f'Average score: {total_grade / solved_problems:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')



