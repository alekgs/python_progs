"""
Декоратор retry

Реализуйте декоратор retry, который принимает один аргумент:
    times — натуральное число

Декоратор должен выполнять повторную попытку вызова декорируемой функции, если во время ее
выполнения возникает ошибка.
Декоратор должен вызывать ее до тех пор, пока не исчерпает количество попыток times,
после чего должен возбуждать исключение MaxRetriesException.
"""

import functools


class MaxRetriesException(Exception):
    ...


def retry(times):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return func(*args, **kwargs)
                except:
                    ...
            raise MaxRetriesException
        return wrapper
    return deco


@retry(3)
def no_way():
    raise ValueError


try:
    no_way()
except Exception as e:
    print(type(e))

# <class '__main__.MaxRetriesException'>


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()

# beegeek
