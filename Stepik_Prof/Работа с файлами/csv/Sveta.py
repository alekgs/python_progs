class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.courses_attached = []

    def rate_hw(self, lecturert, course, grade):
        if isinstance(
                lecturert, Lecturer
        ) and course in self.courses_attached and course in lecturert.courses_in_progress:
            if course in lecturert.grades:
                lecturert.grades[course] += [grade]
            else:
                lecturert.grades[course] = [grade]
        else:
            return 'Ошибка'

    def srgr(self):
        if not self.grades:  # Проверяем что атрибут с оценками (словать) не пустой. Если пустой, то возвращаем 0
            return
        spisok = []  # Определяем пустой список, куда будем складывать оценки (обычная переменная без `self`)
        for g in self.grades.values():  # Проходим в цикле по словарю с оценками (grades), используя "values"
            spisok.extend(g)  # Добавляем в ранее созданный список кортеж, полученный при итерации
        return round(sum(spisok) / len(spisok), 2)
        # Где вместо точек сумму оценок списка делим на длину списка (для этого используем "sum" и "len")

    # def srgr(self):
    #     grades_count = 0
    #     if not self.grades:
    #         return 0
    #     spisok = []
    #     for g in self.grades:
    #         grades_count += len(self.grades[g])
    #         spisok.extent(g)
    #     return float(sum(spisok) / max(len(spisok)))

    def __str__(self):

        courses_in_progress_string = ', '.join(self.courses_in_progress)
        finished_courses_string = ', '.join(self.finished_courses)

        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за домашнее задание:{self.srgr()}\n' \
              f'Курсы в процессе обучени:{courses_in_progress_string}\n' \
              f'Завершенные курсы:{finished_courses_string}'
        return res


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []  # self.courses_attached = []


class Lecturer(Mentor):
    #
    def __init__(self, name, surname, courses_attached):
        super().__init__(name, surname)

        self.grades = {}
        self.srgr = float()
        self.courses_attached = []
        # self.finished_courses = []
        self.courses_in_progress = []

    def srgr(self):
        grades_count = 0
        if not self.grades:
            return 0
        spisok = []
        for g in self.grades.values():
            grades_count += len(self.grades[g])
            spisok.extend(g)
        return float(sum(spisok) / max(len(spisok), 1))

    def __str__(self):
        # res = f'Имя: {self.name}\nФамилия: {self.surname}'
        # return res
        res = f'Имя:{self.name}\n' \
              f'Фамилия:{self.surname}\n' \
              f'Средняя оценка за лекцию :{self.srgr}\n'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такое сравнение некорректно')
            return
        return self.srgr < other.srgr


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):

        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']

# cool_Reviewer = Reviewer('Some', 'Buddy')
# cool_Reviewer.courses_attached += ['Python']

# cool_Reviewer.rate_hw(best_student, 'Python', 10)
# cool_Reviewer.rate_hw(best_student, 'Python', 10)
# cool_Reviewer.rate_hw(best_student, 'Python', 10)

# print(best_student.grades)

student_1 = Student('Кузя', 'Кузнецов', "m")
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Максим', 'Максимов', 'm')
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['Введение в программирование']
print(f'\n\nПеречень студентов:\n\n{student_1}\n\n{student_2}')

lecturert_1 = Lecturer('Иван', 'Иванов', 4)
lecturert_1.courses_in_progress += ['Python']
# lecturert_1.finished_courses += ['Введение в программирование']
lecturert_2 = Lecturer('Сергей', 'Сергеев', 6)
lecturert_2.courses_in_progress += ['Git']
print(f'\n\nПеречень лекторов :\n\n{lecturert_1}\n\n{lecturert_2}')

reviewer_1 = Reviewer('Иван', 'Иванов')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Сергей', 'Сергеев')
reviewer_2.courses_attached += ['Git']

print(f'\n\nПеречень проверяющих :\n\n{reviewer_1}\n\n{reviewer_2}')

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)
reviewer_2.rate_hw(student_2, 'Git', 9)

student_1.rate_hw(lecturert_1, 'Python', 8)
student_1.rate_hw(lecturert_1, 'Python', 9)
student_1.rate_hw(lecturert_1, 'Python', 10)
student_2.rate_hw(lecturert_2, 'Git', 8)
student_2.rate_hw(lecturert_2, 'Git', 7)
student_2.rate_hw(lecturert_2, 'Git', 9)

print(student_1.grades)
print(student_2.grades)
