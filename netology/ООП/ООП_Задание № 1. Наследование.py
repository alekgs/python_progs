"""
Задание № 1. Наследование
Исходя из квиза к предыдущему занятию, у нас уже есть класс преподавателей и класс студентов (вы можете взять этот
код за основу или написать свой). Студентов пока оставим без изменения, а вот преподаватели бывают разные,
поэтому теперь класс Mentor должен стать родительским классом, а от него нужно реализовать наследование классов
Lecturer (лекторы) и Reviewer (эксперты, проверяющие домашние задания). Очевидно, имя, фамилия и список закрепленных
курсов логично реализовать на уровне родительского класса. А чем же будут специфичны дочерние классы? Об этом в
следующих заданиях.
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


# класс Lecturer (лекторы) - дочерний от класса Mentor
class Lecturer(Mentor):
    pass


# класс Reviewer (эксперты, проверяющие домашнее задание) - дочерний от класса Mentor
class Reviewer(Mentor):
    pass


# Создаем студента и его курсы
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

# Преподаватель и его курсы
cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

print(best_student.grades)
