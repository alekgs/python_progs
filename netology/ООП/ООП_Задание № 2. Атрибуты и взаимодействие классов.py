"""
В квизе к предыдущей лекции мы реализовали возможность выставлять студентам оценки за домашние задания. Теперь это
могут делать только Reviewer (реализуйте такой метод)! А что могут делать лекторы? Получать оценки за лекции от
студентов :) Реализуйте метод выставления оценок лекторам у класса Student (оценки по 10-балльной шкале, хранятся в
атрибуте-словаре у Lecturer, в котором ключи – названия курсов, а значения – списки оценок). Лектор при этом должен
быть закреплен за тем курсом, на который записан студент.
"""


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

    def rate_lecturer(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            lectur.grades[course] = lectur.grades.get(course, []) + [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# класс Lecturer (лекторы) - дочерний от класса Mentor
class Lecturer(Mentor):
    grades = {}


# класс Reviewer (эксперты, проверяющие домашнее задание) - дочерний от класса Mentor
class Reviewer(Mentor):
    def rate_hw(self, stud, course, grade):
        if isinstance(stud, Student) and course in self.courses_attached and course in stud.courses_in_progress:
            stud.grades[course] = stud.grades.get(course, []) + [grade]
        else:
            return print('Ошибка')


# Преподаватель и его курсы
some_lecturer = Lecturer('Олег', 'Гежин')
some_lecturer.courses_attached += ['Python']

# Эксперт и его список курсов, по которым он проверяет дом. з
# и выставляет оценки
some_reviewer = Reviewer('Игорь', 'Сверчков')
some_reviewer.courses_attached += ['Python']

# Cтудент и его курсы
some_student = Student('Алексей', 'Саяпин', 'муж.')
some_student.courses_in_progress += ['Python']

# оценка преподавателя
some_student.rate_lecturer(some_lecturer, 'Python', 10)

# Проверяем домашку и выставляем оценки по курсу
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)

# Вывод оценок студента
print(some_student.grades)

# Вывод оценок преподавателя
print(some_lecturer.grades)
