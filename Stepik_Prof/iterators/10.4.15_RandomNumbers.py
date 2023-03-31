"""
Итератор RandomNumbers

Реализуйте класс RandomNumbers, порождающий итераторы, конструктор которого принимает три
аргумента в следующем порядке:

    left — целое число
    right — целое число
    n — натуральное число

Итератор класса RandomNumbers должен генерировать последовательность из n случайных чисел от left
до right включительно, а затем возбуждать исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.
"""
from random import randint


class RandomNumbers:
    def __init__(self, left, right, n):
        self.obj = (randint(left, right) for _ in range(n))

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.obj)


# Sample Input 1:
iterator = RandomNumbers(1, 1, 3)
print(next(iterator))
print(next(iterator))
print(next(iterator))

#print(next(iterator))
#print(next(iterator))

# Sample Output 1:
#
# 1
# 1
# 1
#
# Sample Input 2:
iterator = RandomNumbers(1, 10, 2)
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# Sample Output 2:
#
# True
# True
