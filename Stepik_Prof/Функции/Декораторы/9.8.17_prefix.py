"""
Декоратор prefix

Реализуйте декоратор prefix, который принимает два аргумента в следующем порядке:
    string — произвольная строка
    to_the_end — булево значение, по умолчанию равное False

Декоратор должен добавлять строку string к возвращаемому значению декорируемой функции. Если
to_the_end имеет значение True, строка string добавляется в конец, если False — в начало.

Также декоратор должен сохранять имя и строку документации декорируемой функции.

Примечание 1.
Гарантируется, что возвращаемым значением декорируемой функции является объект типа str.
"""
import functools


def prefix(string, to_the_end=False):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return (f'{string}{res}', f'{res}{string}')[to_the_end]
        return wrapper
    return deco


@prefix('€')
def get_bonus():
    return '500'


print(get_bonus())

# €2000


@prefix('$', to_the_end=True)
def get_bonus():
    return '2000'


print(get_bonus())


# 2000$$$
