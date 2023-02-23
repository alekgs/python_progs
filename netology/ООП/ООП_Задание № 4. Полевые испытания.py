"""
Задание № 4. Полевые испытания
Создайте по 2 экземпляра каждого класса, вызовите все созданные методы, а также реализуйте две функции:
1 - для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса
    (в качестве аргументов принимаем список студентов и название курса);
2 - для подсчета средней оценки за лекции всех лекторов в рамках курса
    (в качестве аргумента принимаем список лекторов и название курса).
"""

# Список для созданных объектов класса Students
students_list = []
# Список для созданных объектов Lecturer
lecturer_list = []
# Список для созданных объектов Reviewers
reviewer_list = []


class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    def add_finish_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in lectur.courses_attached and course in self.courses_in_progress:
            lectur.grades[course] = lectur.grades.get(course, []) + [grade]

    def __str__(self):
        out_string = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        out_string += f'Средняя оценка за домашние задания: {self.get_average_score()}\n'
        out_string += f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n"
        out_string += f"Завершенные курсы: {', '.join(self.finished_courses)}\n"
        return out_string

    def get_average_score(self) -> float:
        """Функция вычисления средней оценки по всем курсам данного объекта"""
        count_courses = len(self.grades)
        if count_courses:
            sum_mean = sum(map(lambda x: sum(x) / len(x), self.grades.values()))
            return round(sum_mean / count_courses, 1)
        return 0

    def __lt__(self, st2):
        if not isinstance(st2, Student):
            return 'Ошибка сравнения'
        return self.get_average_score() < st2.get_average_score()

    def __gt__(self, st2):
        if not isinstance(st2, Student):
            return 'Ошибка сравнения'
        return self.get_average_score() > st2.get_average_score()

    def __eq__(self, st2):
        if not isinstance(st2, Student):
            return 'Ошибка сравнения'
        return self.get_average_score() == st2.get_average_score()


# класс Преподаватели
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
        lecturer_list.append(self)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.get_average_score()}\n'

    def get_average_score(self) -> float:
        """Функция вычисления средней оценки по всем курсам данного объекта"""
        count_courses = len(self.grades)
        if count_courses:
            sum_mean = sum(map(lambda x: sum(x) / len(x), self.grades.values()))
            return round(sum_mean / count_courses, 1)
        return 0

    def __lt__(self, lect2):
        if not isinstance(lect2, Lecturer):
            return 'Ошибка сравнения'
        return self.get_average_score() < lect2.get_average_score()

    def __gt__(self, lect2):
        if not isinstance(lect2, Lecturer):
            return 'Ошибка сравнения'
        return self.get_average_score() > lect2.get_average_score()

    def __eq__(self, lect2):
        if not isinstance(lect2, Lecturer):
            return 'Ошибка сравнения'
        return self.get_average_score() == lect2.get_average_score()


# класс Reviewer (эксперты, проверяющие домашнее задание)
class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        reviewer_list.append(self)

    def rate_hw(self, stud, course, grade):
        if isinstance(stud, Student) and course in self.courses_attached and course in stud.courses_in_progress:
            stud.grades[course] = stud.grades.get(course, []) + [grade]

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'


def get_average_scores_stud(studs: list, course: str):
    get_average_scores(studs, students_list, course, 'студентов')


def get_average_scores_lect(lect: list, course: str):
    get_average_scores(lect, lecturer_list, course, 'за лекции')


def get_average_scores(list1: list, list2: list, course: str, title: str) -> None:
    """Считает средние оценки студентам и преподавателям в рамках конкретного курса"""
    result = {}
    for s in list2:
        list_grades = s.grades.get(course)
        f_name = s.name + ' ' + s.surname
        if f_name in list1 and list_grades:
            count_grades = len(list_grades)
            result[f_name] = (0, round(sum(list_grades) / count_grades, 1))[count_grades >= 1]
    if result:
        get_print_result(title, result, course)
    else:
        print(f'Нет сведений по курсу \"{course}\"')


def get_print_result(title: str, res: dict, course: str):
    str_out = f'\nСредние оценки {title} по курсу: \"{course}\"'
    l_str_out = len(str_out)
    print(str_out, '-' * l_str_out, sep='\n')
    for k, v in res.items():
        spaces = ' ' * (l_str_out - len(k) - len(str(v)) - 1)
        print(f'{k}:{spaces}{v}')


# -------------------- Тестирование программы --------------------------- #

# Преподаватели и их курсы
lecturer1 = Lecturer('Олег', 'Гежин')
lecturer1.courses_attached += ['Python', 'Java', 'SQL', 'C++']

lecturer2 = Lecturer('Олеся', 'Васина')
lecturer2.courses_attached += ['Python', 'Java', 'SQL', 'C++']

# Эксперт и его список курсов, по которым он проверяет дом. задание
# и выставляет оценки
reviewer1 = Reviewer('Игорь', 'Сверчков')
reviewer1.courses_attached += ['Python', 'Java', 'SQL', 'C++']

reviewer2 = Reviewer('Владимир', 'Хомутов')
reviewer2.courses_attached += ['Python', 'Java', 'SQL', 'C++']

# Cтуденты и их курсы
stud1 = Student('Алексей', 'Саяпин', 'муж.')
stud1.courses_in_progress += ['Python', 'SQL', 'C++']

stud2 = Student('Петр', 'Васечкин', 'муж.')
stud2.courses_in_progress += ['Python', 'Java']

stud3 = Student('Анна', 'Каренина', 'жен.')
stud3.courses_in_progress += ['Python', 'C++']

# Законченные курсы у студентов
stud1.add_finish_courses('HTML/CSS')
stud2.add_finish_courses('SQL')
stud3.add_finish_courses('Java')

# Проверка домашки экспертами и выставление оценок студентам по курсам
reviewer1.rate_hw(stud1, 'Python', 10)
reviewer1.rate_hw(stud1, 'Python', 9)

reviewer2.rate_hw(stud2, 'Python', 9)
reviewer2.rate_hw(stud2, 'Python', 5)

reviewer1.rate_hw(stud3, 'Python', 9)
reviewer1.rate_hw(stud3, 'Python', 8)

reviewer2.rate_hw(stud3, 'Python', 8)
reviewer2.rate_hw(stud3, 'Python', 7)

# Оценки лектору lectur1
stud1.rate_lecturer(lecturer1, 'Python', 10)
stud2.rate_lecturer(lecturer1, 'Python', 9)
stud3.rate_lecturer(lecturer1, 'Python', 9)

stud1.rate_lecturer(lecturer2, 'Python', 8)
stud2.rate_lecturer(lecturer2, 'Python', 7)
stud3.rate_lecturer(lecturer2, 'Python', 6)

# Информация о преподавателях (вызов метода __str___)
print('Преподаватели')
[print(lect) for lect in lecturer_list]

# Информация о студентах (вызов метода __str___)
print('Эксперты')
[print(expert) for expert in reviewer_list]

# Информация о студентах (вызов метода __str___)
print('Студенты')
[print(stud) for stud in students_list]

print(f"Сравнение оценок студентов за курсы:")
print(f"{stud1.name} {stud1.surname} "
      f"{'<' if stud1 < stud2 else ('>' if stud1 > stud2 else '=')} "
      f"{stud2.name} {stud2.surname}")

print(f"{stud1.name} {stud1.surname} "
      f"{'<' if stud1 < stud3 else ('>' if stud1 > stud3 else '=')} "
      f"{stud3.name} {stud3.surname}")

print(f"{stud2.name} {stud2.surname} "
      f"{'<' if stud2 < stud3 else ('>' if stud2 > stud3 else '=')} "
      f"{stud3.name} {stud3.surname}")
print()

print(f"Сравнение оценок лекторов за лекции:")
print(f"{lecturer1.name} {lecturer1.surname} "
      f"{'<' if lecturer1 < lecturer2 else ('>' if lecturer1 > lecturer2 else '=')} "
      f"{lecturer2.name} {lecturer2.surname}")
print()


# Вывод списка средних оценок заданных студентов и заданного курса
get_average_scores_stud(['Алексей Саяпин', 'Петр Васечкин', 'Анна Каренина'], 'Python')
get_average_scores_lect(['Олег Гежин', 'Олеся Васина'], 'Python')
