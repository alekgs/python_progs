"""
Задание № 3. Полиморфизм и магические методы

Перегрузите магический метод __str__ у всех классов.

У проверяющих он должен выводить информацию в следующем виде:

print(some_reviewer)
Имя: Some
Фамилия: Buddy

У лекторов:
print(some_lecturer)
Имя: Some
Фамилия: Buddy
Средняя оценка за лекции: 9.9

А у студентов так:
print(some_student)
Имя: Ruoy
Фамилия: Eman
Средняя оценка за домашние задания: 9.9
Курсы в процессе изучения: Python, Git
Завершенные курсы: Введение в программирование


2. Реализуйте возможность сравнивать (через операторы сравнения) между собой лекторов по средней оценке за лекции и
студентов по средней оценке за домашние задания.

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

    def __str__(self):
        out_string = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        out_string += f'Средняя оценка за домашние задания: {calc_average_score(self.grades)}\n'
        out_string += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        out_string += f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return out_string

    def student_average(self):
        """Функция возвращает среднюю оценку студента"""
        return calc_average_score(self.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# класс Lecturer (лекторы)
class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {calc_average_score(self.grades)}\n'

    def lecture_average(self):
        """Функция возвращает среднюю оценку лектора за лекции"""
        return calc_average_score(self.grades)


# класс Reviewer (эксперты, проверяющие домашнее задание)
class Reviewer(Mentor):
    def rate_hw(self, stud, course, grade):
        if isinstance(stud, Student) and course in self.courses_attached and course in stud.courses_in_progress:
            stud.grades[course] = stud.grades.get(course, []) + [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


def calc_average_score(grade_dict: dict) -> float | None:
    """Функция вычисления средней оценки по всем курсам данного объекта"""
    count_courses = len(grade_dict)
    if count_courses:
        sum_mean = sum(map(lambda x: sum(x) / len(x), grade_dict.values()))
        return round(sum_mean / count_courses, 1)
    return


# -------------------- Тестирование программы --------------------------- #

# Преподаватель и его курсы
some_lecturer = Lecturer('Олег', 'Гежин')
some_lecturer.courses_attached += ['Python', 'Java', 'SQL', 'C++']

another_lecturer = Lecturer('Олеся', 'Васина')
another_lecturer.courses_attached += ['Python', 'Java', 'SQL', 'C++']

# Эксперт и его список курсов, по которым он проверяет дом. задание
# и выставляет оценки
some_reviewer = Reviewer('Игорь', 'Сверчков')
some_reviewer.courses_attached += ['Python', 'Java', 'SQL', 'C++']

# Cтудент и его курсы
some_student = Student('Алексей', 'Саяпин', 'муж.')
some_student.courses_in_progress += ['Python', 'Java', 'SQL', 'C++']
some_student.finished_courses += ['HTML/CSS']

# Оценки лектору some_lecturer
some_student.rate_lecturer(some_lecturer, 'Python', 10)
some_student.rate_lecturer(some_lecturer, 'Python', 9)
some_student.rate_lecturer(some_lecturer, 'Java', 8)
some_student.rate_lecturer(some_lecturer, 'Java', 9)
some_student.rate_lecturer(some_lecturer, 'SQL', 9)
some_student.rate_lecturer(some_lecturer, 'SQL', 10)
some_student.rate_lecturer(some_lecturer, 'C++', 9)
some_student.rate_lecturer(some_lecturer, 'C++', 10)

# Оценки лектору another_lecturer
some_student.rate_lecturer(another_lecturer, 'Python', 7)
some_student.rate_lecturer(another_lecturer, 'Python', 8)
some_student.rate_lecturer(another_lecturer, 'SQL', 9)
some_student.rate_lecturer(another_lecturer, 'SQL', 8)
some_student.rate_lecturer(another_lecturer, 'C++', 7)
some_student.rate_lecturer(another_lecturer, 'C++', 8)
some_student.rate_lecturer(another_lecturer, 'Java', 8)
some_student.rate_lecturer(another_lecturer, 'Java', 9)

# Проверка домашки экспертом и выставляем оценки студенту по курсу
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(some_student, 'Python', 10)

# Вывод всех участников процесса обучения
print(some_lecturer)
print(another_lecturer)
print(some_reviewer)
print(some_student)

# Сравнение оценок лекторов
print(some_lecturer.lecture_average() > another_lecturer.lecture_average())
print(some_lecturer.lecture_average() < another_lecturer.lecture_average())
print(some_lecturer.lecture_average() == another_lecturer.lecture_average())

# Сравнение оценок студентов
print(some_student.student_average() > some_student.student_average())
print(some_student.student_average() < some_student.student_average())
print(some_student.student_average() == some_student.student_average())
