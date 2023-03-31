"""
Функция get_min_max() 😳

Реализуйте функцию get_min_max(), которая принимает один аргумент:
    iterable — итерируемый объект, элементы которого сравнимы между собой

Функция должна возвращать кортеж, в котором первым элементом является минимальный элемент
итерируемого объекта iterable, вторым — максимальный элемент итерируемого объекта iterable.
Если итерируемый объект iterable пуст, функция должна вернуть значение None.
"""
from copy import copy


def get_min_max(iterable):
    iter_copy = copy(iterable)
    try:
        return min(iterable), max(iter_copy)
    except ValueError:
        return


# # TEST_1:
iterable = iter(range(10))
print(get_min_max(iterable))
# # (0, 9)
#
# # TEST_2:
iterable = [6, 4, 2, 33, 19, 1]
print(get_min_max(iterable))
# # (1, 33)
#
# TEST_3:
iterable = iter([])
print(get_min_max(iterable))
# None
#
# TEST_4:
data = iter((9, 9, 9, 9, 9))
print(get_min_max(data))
# (9, 9)
#
# # TEST_5:
data = iter(range(1, 101))
print(get_min_max(data))
# # (1, 100)
#
# TEST_6:
data = list(range(1, 101))[::-1]
print(get_min_max(data))
# # (1, 100)
#
# # TEST_7:
data = iter(
    [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79,
     -72, -2, 61, -16, -9, 89, -44, -30])
print(get_min_max(data))
# # (-100, 96)
#
# # TEST_8:
data = iter(
    [-86, -51, 33, -23, 40, 96, 19, -65, 26, 12, -93, 68, 82, 47, -58, -37, -100, 5, 75, 54, -79,
     -72, -2, 61, -16, -9, 89, -44, -30, -100, 96, -100, 1, 2, -99, 96])
print(get_min_max(data))
# # (-100, 96)
#
# # TEST_9:
iterable = []
print(get_min_max(iterable))
# # None
#
# # TEST_10:
iterable = [69]
print(get_min_max(iterable))
# # (69, 69)

# TEST_11:
data = iter(range(100_000_000))
print(get_min_max(data))  # (0, 99999999)

# # TEST_12:
data = iter(['a', 'b', 'c', 'aaa', 'abc', 'cbc', 'bbb'])
print(get_min_max(data))
# # ('a', 'cbc')
#
# # TEST_13:
data = iter(['bbb'])
print(get_min_max(data))  # # ('bbb', 'bbb')
