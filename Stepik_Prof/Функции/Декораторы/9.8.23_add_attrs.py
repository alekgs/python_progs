"""
Декоратор add_attrs

Реализуйте декоратор add_attrs, который принимает произвольное количество именованных аргументов
и устанавливает их в качестве атрибутов декорируемой функции. Названием атрибута должно являться
имя аргумента, значением атрибута — значение аргумента.

"""
import functools


# def add_attrs(**kwargs):
#     return lambda fun: [fun.__dict__.update(kwargs), fun][1]


def add_attrs(**attrs):
    def deco(func):
        func.__dict__ |= attrs

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)

        return wrapper

    return deco


@add_attrs(attr1='bee', attr2='geek')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)


# bee
# geek


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'


print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)

# bee
# geek
# beegeek
