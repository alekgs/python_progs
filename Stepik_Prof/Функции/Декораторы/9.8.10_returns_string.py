"""
Декоратор returns_string

Реализуйте декоратор returns_string, который проверяет, что возвращаемое значение декорируемой
функции принадлежит типу str. Если возвращаемое значение принадлежит какому-либо другому типу,
декоратор должен возбуждать исключение TypeError.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

"""
import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, str):
            raise TypeError
        return result
    return wrapper



@returns_string
def beegeek():
    return 'beegeek'


print(beegeek())

# beegeek


@returns_string
def add(a, b):
    return a + b


try:
    print(add(3, 7))
except TypeError as e:
    print(type(e))


# <class 'TypeError'>
