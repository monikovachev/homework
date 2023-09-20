jury_count = int(input())
presentation_name = input()
grade_sum = 0
all_grades = 0
all_grades_count = 0
while presentation_name != 'Finish':
    grade_sum_avg = 0
    grade_sum = 0
    for _ in range(jury_count):
        grade = float(input())
        grade_sum += grade
        all_grades += grade
        all_grades_count += 1
    grade_sum_avg = grade_sum / jury_count
    print(f'{presentation_name} - {grade_sum_avg:.2f}.')
    presentation_name = input()

if presentation_name == 'Finish':
    print(f'Student\'s final assessment is {all_grades / all_grades_count:.2f}.')
