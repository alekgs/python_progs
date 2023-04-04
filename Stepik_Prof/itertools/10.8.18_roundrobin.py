"""
Функция roundrobin()
Реализуйте функцию roundrobin(), которая принимает произвольное количество позиционных
аргументов, каждый из которых является итерируемым объектом.

Функция должна возвращать итератор, генерирующий последовательность из элементов всех переданных итерируемых
объектов: сначала первый элемент первого итерируемого объекта, затем первый элемент второго итерируемого объекта,
и так далее; после второй элемент первого итерируемого объекта, затем второй элемент второго итерируемого объекта,
и так далее.
"""
from itertools import zip_longest


def roundrobin(*args):
    for a in zip_longest(*args, fillvalue='*'):
        yield from (s for s in a if s != '*')





# Sample Input 1:
print(*roundrobin('abc', 'd', 'ef'))

# Sample Output 1:
# a d e b f c

# Sample Input 2:
numbers = [1, 2, 3]
letters = iter('beegeek')
print(*roundrobin(numbers, letters))

# Sample Output 2:
# 1 b 2 e 3 e g e e k

# Sample Input 3:
print(list(roundrobin()))

# Sample Output 3:
# []

# Test 9
numbers = iter([1, 2, 3])
nones = iter([None, None, None, None])
print(*roundrobin(numbers, nones))
