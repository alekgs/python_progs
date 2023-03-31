"""
Декоратор repeat

Реализуйте декоратор repeat, который принимает один аргумент:
    times — натуральное число

Декоратор должен вызывать декорируемую функцию times раз.
"""
import functools


def repeat(times):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            [func(*args, **kwargs) for _ in range(times - 1)]
            return func(*args, **kwargs)
        return wrapper
    return deco


@repeat(3)
def say_beegeek():
    """documentation"""
    print('beegeek')


say_beegeek()

# beegeek
# beegeek
# beegeek


@repeat(4)
def say_beegeek():
    """documentation"""
    print('beegeek')


print(say_beegeek.__name__)
print(say_beegeek.__doc__)

# say_beegeek
# documentation


# TEST_5:
@repeat(10)
def add(a, b):
    """sum of two numbers"""
    return a + b


print(add.__name__)
print(add.__doc__)
print(add(10, b=20))

# add
# sum of two numbers
# 30
