"""
Функция max_pair()

Реализуйте функцию max_pair(), которая принимает один аргумент:
    iterable — итерируемый объект, элементами которого являются числа

Функция должна возвращать единственное число — максимальную сумму двух соседних чисел итерируемого объекта iterable.

Примечание 1.
Рассмотрим список чисел 1,8,2,4,3 из первого теста.
Из данной последовательности можно получить следующие пары соседних элементов: 1 и 8, 8 и 2, 2 и 4, 4 и 3.
Максимальную сумму имеет вторая пара — 10.
"""

from itertools import pairwise


def max_pair(it):
    return max(map(sum, pairwise(it)))



# Sample Input 1:
print(max_pair([1, 8, 2, 4, 3]))

# Sample Output 1:
# 10

# Sample Input 2:
iterator = iter([1, 2, 3, 4, 5])
print(max_pair(iterator))

# Sample Output 2:
# 9

# Sample Input 3:
iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])
print(max_pair(iterator))

# Sample Output 3:
# 0

