"""
Декоратор reverse_args

Реализуйте декоратор reverse_args, который передает все позиционные аргументы в декорируемую
функцию func в обратном порядке.

Sample Output 1:
9
Sample Output 2:
meloncherryapple
"""


def reverse_args(func):
    def wrapper(*args, **kwargs):
        return func(*args[::-1], **kwargs)
    return wrapper


@reverse_args
def power(a, n):
    return a ** n

print(power(2, 3))


@reverse_args
def concat(a, b, c):
    return a + b + c

print(concat('apple', 'cherry', 'melon'))
