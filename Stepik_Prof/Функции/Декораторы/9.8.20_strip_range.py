"""
Декоратор strip_range

Реализуйте декоратор strip_range, который принимает три аргумента в следующем порядке:
    start — неотрицательное целое число
    end — неотрицательное целое число
    char — одиночный символ, по умолчанию равный точке

Декоратор должен изменять возвращаемое значение декорируемой функции, заменяя все символы
в диапазоне индексов от start (включительно) до end (не включительно) на символ char.

Гарантируется, что start < end.
"""
import functools


def strip_range(start, end, char='.'):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return res[:start] + char * (min(end, len(res)) - start) + res[end:]
        return wrapper
    return deco


@strip_range(3, 5)
def beegeek():
    return 'beegeek'


print(beegeek())


# bee..ek


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())


# bee____


@strip_range(20, 30)
def beegeek():
    return 'beegeek'


print(beegeek())

# beegeek
