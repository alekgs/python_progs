"""
Декоратор sandwich

Реализуйте декоратор sandwich, который выводит тексты:
---- Верхний ломтик хлеба ----

---- Нижний ломтик хлеба ----

до и после вызова декорируемой функции соответственно.

Примечание 1.
Не забывайте про то, что декоратор не должен поглощать возвращаемое значение
декорируемой функции, а также должен уметь декорировать функции с произвольным количеством
позиционных и именованных аргументов.


"""


def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result = func(*args, **kwargs)
        print('---- Нижний ломтик хлеба ----')
        return result
    return wrapper


@sandwich
def add_ingredients(ingredients):
    print(' | '.join(ingredients))


add_ingredients(['томат', 'салат', 'сыр', 'бекон'])


@sandwich
def beegeek():
    return 'beegeek'


print(beegeek())


@sandwich
def counter(*args, **kwargs):
    for i in args + tuple(kwargs.keys()) + tuple(kwargs.values()):
        print(i)


counter(10, 20, 30, sep='40', end='!!!', step='beegeek')