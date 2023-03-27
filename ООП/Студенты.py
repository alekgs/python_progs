class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_finish_courses(self, course_name):
        self.finished_courses.append(course_name)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            student.grades[course] = student.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'


# Преподаватель и его курсы
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']
cool_mentor.courses_attached += ['C++']
cool_mentor.courses_attached += ['Java']
cool_mentor.courses_attached += ['SQL']
# print(cool_mentor.courses_attached)

# Создаем первого студента и его курсы
student1 = Student('Иван', 'Петров', 'М')
student1.courses_in_progress += ['Python']
student1.courses_in_progress += ['SQL']

# Создаем второго студента и его курсы
student2 = Student('Света', 'Иванова', 'Ж')
student2.courses_in_progress += ['C++']
student2.courses_in_progress += ['Python']

# Ставим оценку студенту1 по курсу Python и SQL
cool_mentor.rate_hw(student1, 'Python', 10)
cool_mentor.rate_hw(student1, 'Python', 10)
cool_mentor.rate_hw(student1, 'SQL', 10)

# Ставим оценку студенту2 по курсу Python и C++
cool_mentor.rate_hw(student2, 'Python', 10)
cool_mentor.rate_hw(student2, 'C++', 10)

# Выводим студентов, их курсы и оценки (НАПИСАТЬ функцию вывода!)
print('Студент: ', student1.name, student1.surname, student1.gender)
print('Изучает: ', *student1.courses_in_progress, sep=', ')
print('Оценки: ', student1.grades)
print('Закончены: ', *student1.finished_courses)
print()
print('Студент: ', student2.name, student2.surname, student2.gender)
print('Изучает: ', *student2.courses_in_progress, sep=', ')
print('Оценки: ', student2.grades)
print('Закончены: ', *student2.finished_courses)


