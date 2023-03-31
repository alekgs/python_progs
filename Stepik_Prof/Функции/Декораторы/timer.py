"""
Декоратор timer

Подсчитывает время выполнения функции.
Для более точного подсчета декоратор принимает аргумент iters, который задает количество измерений
"""

import functools
import time


def timer(iters=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.perf_counter()
                value = func(*args, **kwargs)
                end = time.perf_counter()
                total += end - start
            print(f'Среднее время выполнения {func.__name__}: {round(total / iters, 4)} сек.')
            return value

        return wrapper

    return decorator


@timer(iters=1000)
def test(n):
    return sum([(i / 99) ** 2 for i in range(n)])


@timer(iters=3)
def sleep(n):
    time.sleep(n)


res1 = test(10000)
res2 = sleep(4)

print(f'Результат функции test = {res1}')
print(f'Результат функции sleep = {res2}')
