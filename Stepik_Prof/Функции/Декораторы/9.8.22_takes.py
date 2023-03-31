"""
Декоратор takes.

Реализуйте декоратор takes, который принимает произвольное количество
позиционных аргументов, каждый из которых является типом данных.

Декоратор должен проверять, что аргументы, передаваемые в декорируемую функцию, принадлежат
одному из этих типов. Если хотя бы один аргумент не принадлежит одному из данных типов, декоратор
должен возбуждать исключение TypeError.
"""
import functools


def takes(*arg_list):
    def deco(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not all(map(lambda x: isinstance(x, arg_list), (*args, *kwargs.values()))):
                raise TypeError
            return func(*args, **kwargs)
        return wrapper
    return deco


@takes(int, str)
def repeat_string(string, times):
    return string * times


print(repeat_string('bee', 3))


# beebeebee


@takes(list, bool, float, int)
def repeat_string(string, times):
    return string * times


try:
    print(repeat_string('bee', 4))
except TypeError as e:
    print(type(e))


# <class 'TypeError'>


# TEST_6:
@takes(list, int, tuple, str)
def add(a, b):
    """add docs"""
    return a + b


print(add.__name__)
print(add.__doc__)

try:
    print(add(a='a', b='c'))
except TypeError as e:
    print(type(e))


# TEST_6:
# add
# add docs
# ac

# TEST_11:
@takes(str)
def beegeek(word, repeat):
    return word * repeat


try:
    print(beegeek('beegeek', repeat=2))
except TypeError as e:
    print(type(e))

# <class 'TypeError'>
