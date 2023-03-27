"""
Функция numbers_sum()

Реализуйте функцию numbers_sum(), которая принимает один аргумент:
    elems — список произвольных объектов

Функция должна возвращать сумму чисел (типы int и float), находящихся в списке elems,
игнорируя все нечисловые объекты. Если в списке elems нет чисел, функция должна вернуть число 0.

Также функция должна иметь следующую строку документации:

Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.


Sample Input 1:
print(numbers_sum([1, '2', 3, 4, 'five']))

Sample Output 1:

8

Sample Input 2:
print(numbers_sum(['beegeek', 'stepik', '100']))

Sample Output 2:
0

Sample Input 3:
print(numbers_sum.__doc__)

Sample Output 3:
Принимает список и возвращает сумму его чисел (int, float),
игнорируя нечисловые объекты. 0 - если в списке чисел нет.
"""


def numbers_sum(elems) -> int or float:
    """
    Принимает список и возвращает сумму его чисел (int, float),
    игнорируя нечисловые объекты. 0 - если в списке чисел нет.
    """

    return sum(i for i in elems if isinstance(i, (int, float)))


print(numbers_sum([1, '2', 3, 4, 'five']))
print(numbers_sum(['beegeek', 'stepik', '100']))
print(numbers_sum.__doc__)
