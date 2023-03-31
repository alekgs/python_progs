"""
Функция get_min_max() 😎

Реализуйте функцию get_min_max(), которая принимает один аргумент:

    data — список произвольных объектов, сравнимых между собой

Функция должна возвращать кортеж, в котором первым элементом является индекс минимального
элемента в списке data, вторым — индекс максимального элемента в списке data. Если список data
пуст, функция должна вернуть значение None.

Примечание 1.
Если минимальных / максимальных элементов несколько, следует вернуть индексы
первого по порядку элемента.
"""


# def get_min_max(data):
#     if data:
#         return data.index(min(data)), data.index(max(data))


# def get_min_max(data):
#     if data:
#         d = dict(enumerate(data))
#         return min(d, key=d.get), max(d, key=d.get)


def get_min_max(data):
    if data:
        return min(enumerate(data), key=lambda x: x[1])[0], \
            max(enumerate(data), key=lambda x: x[1])[0]


data = [2, 3, 8, 1, 7]
print(get_min_max(data))
# (3, 2)

data = [1, 1, 2, 3, 8, 8]
print(get_min_max(data))
# (0, 4)

data = [9]
print(get_min_max(data))
# (0, 0)

data = []
print(get_min_max(data))
