"""
Декоратор trace

Реализуйте декоратор trace, который выводит отладочную информацию о декорируемой функции во время
ее выполнения, а именно: имя функции, переданные аргументы и возвращаемое значение в следующем
формате:

TRACE: вызов <имя функции>() с аргументами: <кортеж позиционных аргументов>, <словарь именованных
аргументов>
TRACE: возвращаемое значение <имя функции>(): <возвращаемое значение>

Также декоратор должен сохранять имя и строку документации декорируемой функции.
"""
import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        print(f'TRACE: возвращаемое значение {func.__name__}():', repr(result))
        return result
    return wrapper


@trace
def say(name, line):
    return f'{name}: {line}'


say('Jane', 'Hello, World')


# TRACE: вызов say() с аргументами: ('Jane', 'Hello, World'), {}
# TRACE: возвращаемое значение say(): 'Jane: Hello, World'


@trace
def sub(a, b, c):
    """прекрасная функция"""
    return a - b + c


print(sub.__name__)
print(sub.__doc__)
sub(20, 5, c=10)


# sub
# прекрасная функция
# TRACE: вызов sub() с аргументами: (20, 5), {'c': 10}
# TRACE: возвращаемое значение sub(): 25


# TEST_3:
@trace
def beegeek():
    """beegeek docs"""
    return 'beegeek'


print(beegeek())
print(beegeek.__name__)
print(beegeek.__doc__)


# TRACE: вызов beegeek() с аргументами: (), {}
# TRACE: возвращаемое значение beegeek(): 'beegeek'
# beegeek
# beegeek
# beegeek docs


# TEST_4:
@trace
def add(a, b, c):
    """docs"""
    return a + b + c

print(add(1, 2, 3))
print(add.__name__)
print(add.__doc__)

# TEST_4:
# TRACE: вызов add() с аргументами: (1, 2, 3), {}
# TRACE: возвращаемое значение add(): 6
# 6
# add
# docs