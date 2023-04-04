"""
Функция grouper()

Реализуйте функцию grouper(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность,
элементами которой являются объединенные в кортежи по n элементов
соседние элементы итерируемого объекта iterable.

Если у элемента недостаточно соседей, то ими становится значение None.

"""

from itertools import zip_longest, repeat


def grouper(it, n):
    return zip_longest(*repeat(iter(it), n))


# Sample Input 1:
numbers = [1, 2, 3, 4, 5, 6]
print(*grouper(numbers, 2))

# Sample Output 1:
# (1, 2) (3, 4) (5, 6)

# Sample Input 2:
iterator = iter([1, 2, 3, 4, 5, 6, 7])
print(*grouper(iterator, 3))

# Sample Output 2:
# (1, 2, 3) (4, 5, 6) (7, None, None)

# Sample Input 3:
iterator = iter([1, 2, 3])
print(*grouper(iterator, 5))

# Sample Output 3:
# (1, 2, 3, None, None)
