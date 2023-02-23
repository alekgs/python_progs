"""
Функция is_correct()
Реализуйте функцию is_correct(), которая принимает три аргумента в следующем порядке:
    day — натуральное число, день
    month — натуральное число, месяц
    year — натуральное число, год

Функция должна возвращать True, если дата с компонентами day, month и year является корректной, или False в противном
случае.

Примечание 1.
Вспомните про конструкцию try-except.

Sample Input 1:
print(is_correct(31, 12, 2021))

Sample Output 1:
True

Sample Input 2:
print(is_correct(31, 13, 2021))

Sample Output 2:
False
"""


# def is_correct(*args):
def is_correct(d: int, m: int, y: int) -> bool:
    """
    Возвращает True, если дата с компонентами day, month и year является корректной,
    или False в противном случае
    """
    try:
        # return bool(__import__('datetime').date(*args[::-1]))
        return bool(__import__('datetime').date(y, m, d))
        # return bool(date(y, m, d))
    except ValueError:
        return False


# Тесты
print(is_correct(31, 12, 2021))
print(is_correct(31, 13, 2021))



