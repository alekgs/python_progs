"""
Функция all_together()

Реализуйте функцию all_together() с использованием генераторных выражений, которая принимает произвольное количество
позиционных аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать генератор, порождающий каждый элемент всех переданных итерируемых объектов: сначала все
элементы первого итерируемого объекта, затем второго, и так далее.

Примечание 1. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


def all_together(*args):
    # for i in args:
    #     yield from i
    return (i for it in args for i in it)


# Sample Input 1:
objects = [range(3), 'bee', [1, 3, 5], (2, 4, 6)]
print(*all_together(*objects))

# Sample Output 1:
# 0 1 2 b e e 1 3 5 2 4 6

# Sample Input 2:
objects = [[1, 2, 3], [(0, 0), (1, 1)], {'geek': 1}]
print(*all_together(*objects))

# Sample Output 2:
# 1 2 3 (0, 0) (1, 1) geek

# Sample Input 3:
print(list(all_together()))


# Sample Output 3:
# []
