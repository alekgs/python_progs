"""
Функция convert()

Реализуйте функцию convert(), которая принимает один аргумент string — произвольная строка

Функция должна возвращать строку string:
    полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
    полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
    полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает

Примечание 1. Символы строки, не являющиеся буквами, следует игнорировать.

Sample Input 1:
print(convert('BEEgeek'))

Sample Output 1:
beegeek

Sample Input 2:
print(convert('pyTHON'))

Sample Output 2:
PYTHON

Sample Input 3:
print(convert('pi31415!'))

Sample Output 3:
pi31415!

"""
from re import findall


def convert(string: str) -> str or None:
    """
    Функция должна возвращать строку string:
    полностью в нижнем регистре, если букв в нижнем регистре в этой строке больше
    полностью в верхнем регистре, если букв в верхнем регистре в этой строке больше
    полностью в нижнем регистре, если количество букв в верхнем и нижнем регистрах в этой строке совпадает
    Символы строки, не являющиеся буквами, следует игнорировать.
    """

    chr_lower = len(findall(r'([a-z])', string))
    chr_upper = len(findall(r'([A-Z])', string))

    return (string.upper(), string.lower())[chr_lower >= chr_upper]

# def convert(string):
#     if sum((-1, 1)[c.isupper()] for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()

# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()

# def convert(string):
#     if sum(map(str.islower, string)) >= sum(map(str.isupper, string)):
#         return string.lower()
#     return string.upper()

# def convert(string):
#     low = [i for i in string if i.islower()]
#     up = [i for i in string if i.isupper()]
#     return (string.lower(), string.upper())[len(low) < len(up)]

# def convert(string):
#     k = 0
#     for i in filter(str.isalpha, string):
#         k = (k+1, k-1)[i.islower()]
#     return (string.lower(), string.upper())[k > 0]


# Тесты
print(convert('BEEgeek'))
print(convert('pyryTHON'))
print(convert('piPI31415!'))
print(convert('ПРивед МедвеД 31415!'))
