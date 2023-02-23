"""
Напишите функцию call(), которая принимает произвольную функцию и аргументы для неё и делает вызов переданной
функции, возвращая ее значение.

Примечание 1.
Приведенный ниже код, при условии, что функция call() написана правильно

def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))

должен выводить:

70
9
80
False
"""


def call(f: callable, *args) -> int or None:
    """Принимает произвольную функцию и аргументы для неё и делает вызов переданной функции, возвращая ее значение """
    return f(*args)


def mul7(x):
    return x * 7


def add2(x, y):
    return x + y


def add3(x, y, z):
    return x + y + z


print(call(mul7, 10))
print(call(add2, 2, 7))
print(call(add3, 10, 30, 40))
print(call(bool, 0))
