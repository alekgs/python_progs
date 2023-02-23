"""
Перепишите функцию product_of_odds() в функциональном стиле с использованием встроенных функций filter() и reduce().

def product_of_odds(data):   # data - список целых чисел
    result = 1
    for i in data:
        if i % 2 == 1:
            result *= i
    return result
"""
from functools import reduce


def product_of_odds(data: list) -> int:
    return reduce(lambda x, y: x * y, filter(lambda x: x % 2, data), 1)


#  функция должна вернуть 945
print(product_of_odds([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(product_of_odds([]))
