students_count = int(input())
grade_total = 0
group1 = 0
group2 = 0
group3 = 0
group4 = 0

for _ in range(students_count):
    grade = float(input())
    grade_total += grade
    if 2 <= grade <= 2.99:
        group1 += 1
    elif 3 <= grade <= 3.99:
        group2 += 1
    elif 4 <= grade <= 4.99:
        group3 += 1
    else:
        group4 += 1

avg_grade = grade_total / students_count

print(f'Top students: {group4 / students_count * 100 :.2f}%')
print(f'Between 4.00 and 4.99: {group3 / students_count * 100 :.2f}%')
print(f'Between 3.00 and 3.99: {group2 / students_count * 100 :.2f}%')
print(f'Fail: {group1 / students_count * 100 :.2f}%')
print(f'Average: {avg_grade:.2f}')
