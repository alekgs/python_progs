"""
Функция first_true()

Реализуйте функцию first_true(), которая принимает два аргумента в следующем порядке:

    iterable — итерируемый объект
    predicate — функция-предикат; если имеет значение None, то работает аналогично функции bool()

Функция first_true() должна возвращать первый по счету элемент итерируемого объекта iterable, для которого функция
predicate вернула значение True. Если такого элемента нет, функция first_true() должна вернуть значение None.

Примечание 1.
Предикат — это функция, которая возвращает True или False в зависимости от переданного в качестве
аргумента значения.

"""
from itertools import dropwhile


def first_true(it, pr):
    if pr is None:
        pr = bool
    return next(dropwhile(lambda elem: not pr(elem), it), None)


# def first_true(it, pr):
#     return next(filter(pr, it), None)



# Sample Input 1:
numbers = [1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))

# Sample Output 1:
# 2

# Sample Input 2:
numbers = iter([1, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200])
print(first_true(numbers, lambda num: num > 10))

# Sample Output 2:
# 100

# Sample Input 3:
numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)
print(first_true(numbers, None))

# Sample Output 3:
# 69
