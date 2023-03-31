"""
Декоратор square

Реализуйте декоратор square, который возводит возвращаемое значение декорируемой функции во
вторую степень.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1. Гарантируется, что возвращаемым значением декорируемой функции является объект типа
int или float.



"""
import functools


def square(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) ** 2

    return wrapper


@square
def add(a, b):
    return a + b


print(add(3, 7))


# 100


@square
def add(a, b):
    """прекрасная функция"""
    return a + b


print(add(1, 1))
print(add.__name__)
print(add.__doc__)

# 4
# add
# прекрасная функция
