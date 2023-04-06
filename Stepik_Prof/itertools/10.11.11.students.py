"""
Вам доступен именованный кортеж Student, который содержит данные об ученике.
Первым элементом именованного кортежа является фамилия ученика, вторым — имя, третьим — класс.
Также доступен список students, содержащий эти кортежи.

Дополните приведенный ниже код, чтобы он вывел наиболее часто
встречаемое имя среди учеников из данного списка.

Примечание. Гарантируется, что искомое имя единственное.

"""

from collections import namedtuple
from itertools import groupby

# from collections import Counter

Student = namedtuple('Student', ['surname', 'name', 'grade'])

students = [Student('Гагиев', 'Александр', 10), Student('Дедегкаев', 'Илья', 11),
            Student('Кодзаев', 'Георгий', 10), Student('Набокова', 'Алиса', 11),
            Student('Кораев', 'Артур', 10), Student('Шилин', 'Александр', 11),
            Student('Уртаева', 'Илина', 11), Student('Салбиев', 'Максим', 10),
            Student('Капустин', 'Илья', 11), Student('Гудцев', 'Таймураз', 11),
            Student('Перчиков', 'Максим', 10), Student('Чен', 'Илья', 11),
            Student('Елькина', 'Мария', 11), Student('Макоев', 'Руслан', 11),
            Student('Албегов', 'Хетаг', 11), Student('Щербак', 'Илья', 10),
            Student('Идрисов', 'Баграт', 11), Student('Гапбаев', 'Герман', 10),
            Student('Цивинская', 'Анна', 10), Student('Туткевич', 'Юрий', 11),
            Student('Мусиков', 'Андраник', 11), Student('Гадзиев', 'Георгий', 11),
            Student('Белов', 'Юрий', 11), Student('Акоева', 'Диана', 11),
            Student('Денисов', 'Илья', 11), Student('Букулова', 'Диана', 10),
            Student('Акоева', 'Лера', 11)]

f = lambda x: x.name
result = groupby(sorted(students, key=f), key=f)
print(max(result, key=lambda x: sum(1 for _ in x[1]))[0])

# # Counter
# print(Counter(i.name for i in students).most_common()[0][0])

# решение № 1
# count_names = []
# for _, names in result:
#     [count_names.append(i.name) for i in names]
#
# d = Counter(count_names)
# print(max(d, key=d.get))

# решение № 2
# d = {}
# for key, values in result:
#     d[key] = d.get(key, 0) + sum(1 for _ in values)
# print(max(d, key=d.get))
