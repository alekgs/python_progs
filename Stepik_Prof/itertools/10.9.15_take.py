"""
Функция take()

Реализуйте функцию take(), которая принимает два аргумента в следующем порядке:
    iterable — итерируемый объект
    n — натуральное число

Функция должна возвращать итератор, генерирующей последовательность из первых n элементов
итерируемого объекта iterable.
"""
from itertools import islice


def take(it, n):
    yield from islice(it, n)


# Sample Input 1:
print(*take(range(10), 5))

# Sample Output 1:
# 0 1 2 3 4

# Sample Input 2:
iterator = iter('beegeek')
print(*take(iterator, 22))

# Sample Output 2:
# b e e g e e k

# Sample Input 3:

iterator = iter('beegeek')
print(*take(iterator, 1))

# Sample Output 3:
# b
