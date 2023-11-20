class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        avg = sum(self.grades) / len(self.students)
        return float(f'{avg:.2f}')

    def __repr__(self):
        students_separated = ', '.join(self.students)
        avg = self.get_average_grade()
        return f'The students in {self.name}: {students_separated}. Average grade: {avg}'
