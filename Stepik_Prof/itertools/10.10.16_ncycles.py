"""
Функция ncycles()

Реализуйте функцию ncycles(), которая принимает два аргумента в следующем порядке:
    iterable — итерируемый объект
    times — натуральное число

Функция должна возвращать итератор, генерирующий последовательность элементов итерируемого
объекта iterable, зацикленных times раз.
"""

from itertools import chain, tee


def ncycles(it, times):
    return chain(*tee(it, times))


# Sample Input 1:
print(*ncycles([1, 2, 3, 4], 3))

# Sample Output 1:
# 1 2 3 4 1 2 3 4 1 2 3 4

# Sample Input 2:
iterator = iter('bee')
print(*ncycles(iterator, 4))

# Sample Output 2:
# b e e b e e b e e b e e

# Sample Input 3:
iterator = iter([1])
print(*ncycles(iterator, 10))

# Sample Output 3:
# 1 1 1 1 1 1 1 1 1 1
