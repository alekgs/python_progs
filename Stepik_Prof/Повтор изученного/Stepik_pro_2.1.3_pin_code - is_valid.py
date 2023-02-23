"""
Функция is_valid()

Будем считать, что PIN-код является корректным, если он удовлетворяет следующим условиям:

    состоит из 44, 55 или 66 символов
    состоит только из цифр (0−90−9)
    не содержит пробелов

Реализуйте функцию is_valid(), которая принимает один аргумент:

    string — произвольная строка

Функция должна возвращать значение True, если строка string представляет собой корректный PIN-код, или False в
противном случае.

Примечание 1. Если в функцию передается пустая строка, функция должна возвращать значение False.
Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию is_valid(), но не код,
вызывающий ее.

Sample Input 1:
print(is_valid('4367'))

Sample Output 1:
True

Sample Input 2:
print(is_valid('92134'))

Sample Output 2:
True

Sample Input 3:
print(is_valid('89abc1'))

Sample Output 3:
False

Sample Input 4:
print(is_valid('900876'))

Sample Output 4:
True

Sample Input 5:
print(is_valid('49 83'))

Sample Output 5:
False

"""

# import re


# def is_valid(string: str) -> bool:
#     """Возвращает True, если строка string представляет собой корректный PIN-код,
#        или False в противном случае"""
#     if len(string) in range(4, 7):
#         s = [i for i in string if i.isdigit()]
#         return len(s) == len(string)
#         # s = fa(r'\d{4,6}', string)
#     return False


# # is_valid = lambda s: [False, True][len(fa(r'\d{4,6}', s))]
from re import fullmatch
is_valid = lambda s: (False, True)[bool(fullmatch('^[0-9]{4,6}?$', s))]


# def is_valid(pin: str) -> bool:
#     return pin.isdigit() and len(pin) in (4, 5, 6)


print(is_valid('4367'))
print(is_valid('921346'))
print(is_valid('89abc1'))
print(is_valid('900876asadd'))
print(is_valid('4983'))
