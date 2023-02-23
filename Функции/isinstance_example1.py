"""
Ваша задача написать функцию find_keys, которая принимает произвольное количество именованных аргументов.
Функция должна отобрать только те имена параметров, у которых значения являются списками или кортежами.
Функция find_keys должна собрать все имена таких параметров в список, отсортировать их по алфавиту
вне зависимости от регистра букв и вернуть в качестве результата.

Ниже представлены примеры:
find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) => ['A', 'b', 't', 'W']
find_keys(name='Bruce', surname='Wayne') => []
find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) => ['Also', 'marks']
"""


def find_keys(**kwargs):
    # return sorted([i for i, k in kwargs.items() if isinstance(k, (list, tuple))], key=str.lower)
    return sorted(filter(lambda s: isinstance(kwargs[s], (list, tuple)), kwargs), key=str.lower)


print(find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]))
print(find_keys(name='Bruce', surname='Wayne'))
print(find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)))
