name_student = input()
bad_tries = 0
current_class = 1
grade_sum = 0

while current_class <= 12:
    grade = float(input())
    if grade < 4:
        bad_tries += 1
        if bad_tries > 1:
            break
        continue
    current_class += 1
    grade_sum += grade

if current_class < 12:
    print(f'{name_student} has been excluded at {current_class} grade')
else:
    avg_grade = grade_sum / 12
    print(f'{name_student} graduated. Average grade: {avg_grade:.2f}')


