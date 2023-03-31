"""
Декоратор ignore_exception

Реализуйте декоратор ignore_exception, который принимает произвольное количество позиционных
аргументов — типов исключений, и выводит текст:

"Исключение <тип исключения> обработано"

если во время выполнения декорируемой функции было
возбуждено исключение, принадлежащее одному из переданных типов.

Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть
возбуждено снова.
"""
import functools


def ignore_exception(*attrs):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except attrs as err:
                print(f'Исключение {type(err).__name__} обработано')
        return wrapper

    return deco


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def f(x):
    return 1 / x


f(0)

# Исключение ZeroDivisionError обработано


min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))

# <class 'TypeError'>


# TEST_9:
@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    return 'beegeek'


print(beegeek())

# TEST_9:
# beegeek