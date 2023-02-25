"""
Напишите декоратор add_args, который добавляет к переданным аргументам еще два значения:
строку begin в начало аргументов, строку end в конец.

Также декоратор должен сохранить первоначальное имя декорируемой функцию и ее строку
документации

Sample Output:
begin, hello, world, my, name is, Artem, end
"""

# Напишите определение декоратора add_args
# Код ниже не удаляйте, он нужен для проверки
from functools import wraps


def add_args(func):
    @wraps(func)
    def inner(*args):
        return func('begin', *args, 'end')

    return inner


@add_args
def concatenate(*args):
    """
    Возвращает конкатенацию переданных строк
    """
    # s = ['begin', *args, 'end']
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Возвращает слово максимальной длины
    """
    return max(args, key=len)


print(concatenate('hello', 'world', 'my', 'name is', 'Artem'))
assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
assert concatenate.__name__ == 'concatenate'
assert concatenate.__doc__.strip() == """Возвращает конкатенацию переданных строк"""
assert find_max_word('my') == 'begin'
assert find_max_word('my', 'how') == 'begin'
assert find_max_word('my', 'how', 'maximum') == 'maximum'
assert find_max_word.__name__ == 'find_max_word'
assert find_max_word.__doc__.strip() == """Возвращает слово максимальной длины"""
