"""
Функция sum_of_digits()

Реализуйте функцию sum_of_digits(), которая принимает один аргумент:
    iterable — итерируемый объект, элементами которого являются натуральные числа

Функция должна возвращать единственное число — сумму цифр всех чисел, присутствующих в итерируемом объекте iterable.

Примечание 1.
Рассмотрим набор чисел 13,20,41,2,2,5 из первого теста.
Сумма цифр всех представленных чисел будет равна:
1+3+2+0+4+1+2+2+5=20
"""
from itertools import chain


def sum_of_digits(it):
    strings = map(str, it)
    all_elements = chain.from_iterable(strings)
    int_digits = map(int, all_elements)
    return sum(int_digits)


# Sample Input 1:
print(sum_of_digits([13, 20, 41, 2, 2, 5]))

# Sample Output 1:
# 20

# Sample Input 2:
print(sum_of_digits((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))

# Sample Output 2:
# 46

# Sample Input 3:
print(sum_of_digits([123456789]))

# Sample Output 3:
# 45
