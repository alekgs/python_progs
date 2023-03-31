"""
Функция reverse()

Реализуйте генераторную функцию reverse(), которая принимает один аргумент:
    sequence — последовательность

Функция должна возвращать генератор, порождающий элементы последовательности sequence в обратном
порядке, а затем возбуждающий исключение StopIteration.

Примечание 1.
Последовательностью является коллекция, поддерживающая индексацию и имеющая длину.
Например, объекты типа list, str, tuple являются последовательностями.
"""


def reverse(sequence):
    yield from sequence[::-1]


# Sample Input 1:
print(*reverse([1, 2, 3, 4, 5]))

# Sample Output 1:
# 5 4 3 2 1

# Sample Input 2:
generator = reverse('beegeek')
print(type(generator))
print(*generator)

# Sample Output 2:
# <class 'generator'>
# k e e g e e b
