number_rows = int(input())
grades_book = {}

for _ in range(number_rows):
    name = input()
    grade = float(input())
    if name not in grades_book.keys():
        grades_book[name] = []
        grades_book[name].append(grade)
    else:
        grades_book[name].append(grade)

for name, grade in grades_book.items():
    avg_grade = sum(grades_book[name]) / len(grades_book[name])
    if avg_grade >= 4.50:
        print(f'{name} -> {avg_grade:.2f}')
