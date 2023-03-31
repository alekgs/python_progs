"""
Функция all_together()

Реализуйте функцию count_iterable() с использованием генераторных выражений, которая принимает один аргумент:
    iterable — итерируемый объект

Функция должна возвращать единственное число — количество элементов итерируемого объекта iterable.

Примечание 1. Гарантируется, что передаваемый в функцию итерируемый объект является конечным.
"""


def count_iterable(iterable):
    return sum(1 for _ in iterable)


# Sample Input 1:
print(count_iterable([1, 2, 3, 4, 5]))

# Sample Output 1:
# 5

# Sample Input 2:
numbers = iter([1, 2, 3, 4, 5, 6, 7])
print(count_iterable(numbers))

# Sample Output 2:
# 7

# Sample Input 3:
data = tuple(range(432, 3845, 17))
print(count_iterable(data))

# Sample Output 3:
# 201
