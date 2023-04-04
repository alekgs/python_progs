"""

Функция first_true()

Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()

Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1. Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве аргумента значения.

Примечание 2. Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.

Примечание 3. В тестирующую систему сдайте программу, содержащую только необходимую функцию first_true(), но не код, вызывающий ее.

Примечание 4. Тестовые данные доступны по ссылкам:

    Архив с тестами
    GitHub

Sample Input 1:

numbers = [1, 1, 1, 1, 2, 4, 5, 6]

print(first_true(numbers, lambda num: num % 2 == 0))

Sample Output 1:

2

Sample Input 2:

numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])

print(first_true(numbers, lambda num: num > 10))

Sample Output 2:

100

Sample Input 3:

numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))

Sample Output 3:

69


"""
from itertools import dropwhile


def drop_this(it, obj):
    yield from dropwhile(lambda s: s == obj, it)


# Sample Input 1:
numbers = [0, 0, 0, 1, 2, 3]
print(*drop_this(numbers, 0))

# Sample Output 1:
# 1 2 3

# Sample Input 2:
iterator = iter('bbbbeebee')
print(*drop_this(iterator, 'b'))

# Sample Output 2:
# e e b e e

# Sample Input 3:
iterator = iter('ssssssssssssssssssssssss')
print(list(drop_this(iterator, 's')))

# Sample Output 3:
# []
