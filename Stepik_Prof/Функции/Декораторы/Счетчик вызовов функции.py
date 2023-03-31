"""
Декоратор отслеживания количества вызовов функции
"""

import functools


def counter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.num += 1
        print(f'Вызов {func.__name__}: {wrapper.num}')
        val = func(*args, **kwargs)
        return val

    wrapper.num = 0
    return wrapper


@counter
def greet(name):
    return f'Hello {name}!'


print(greet('Timur'))
print(greet('Ruslan'))
print(greet('Arthur'))
print(greet('Gvido'))
