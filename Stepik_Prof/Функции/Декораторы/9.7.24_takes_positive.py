"""
Декоратор takes_positive

Реализуйте декоратор takes_positive, который проверяет, что все аргументы, передаваемые в
декорируемую функцию, являются положительными целыми числами.

Если хотя бы один аргумент не удовлетворяет данному условию, декоратор должен возбуждать исключение:
    TypeError, если аргумент не является целым числом
    ValueError, если аргумент является целым числом, но отрицательным или равным нулю

Примечание 1.
Приоритет возбуждения исключений при несоответствии аргумента обоим условиям или
при наличии разных аргументов, несоответствующих разным условиям: TypeError, затем ValueError.

"""


def takes_positive(func):
    def wrapper(*args, **kwargs):
        for v in args + tuple(kwargs.values()):
            # for v in [*args, *kwargs.values()]:
            if not isinstance(v, int):
                raise TypeError
            elif v <= 0:
                raise ValueError
        return func(*args, **kwargs)

    return wrapper


# def takes_positive(func):
#     def wrapper(*args, **kwargs):
#         if args:
#             if not all([isinstance(x, int) for x in args]):
#                 raise TypeError
#             if not all([x > 0 for x in args]):
#                 raise ValueError
#         if kwargs:
#             if not all([isinstance(v, int) for v in kwargs.values()]):
#                 raise TypeError
#             if not all([x > 0 for x in kwargs.values()]):
#                 raise ValueError
#
#         return func(*args, **kwargs)
#     return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)


print(positive_sum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# Sample Output 1:
# 55


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum(-3, -2, -1, 0, 1, 2, 3))
except Exception as err:
    print(type(err))


# Sample Output 2:
# <class 'ValueError'>


@takes_positive
def positive_sum(*args):
    return sum(args)


try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))

# <class 'TypeError'>
