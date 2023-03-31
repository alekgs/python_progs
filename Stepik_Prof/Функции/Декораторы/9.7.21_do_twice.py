"""
Декоратор do_twice
Реализуйте декоратор do_twice, вызывающий декорируемую функцию два раза.

Примечание 1.
Не забывайте про то, что декоратор не должен поглощать возвращаемое значение
декорируемой функции, а также должен уметь декорировать функции с произвольным количеством
позиционных и именованных аргументов.
"""

# ООП
# class do_twice:
#     def __init__(self, func, repeats=2):
#         self.func = func
#         self.repeats = repeats
#
#     def __call__(self, *args, **kwargs):
#         for _ in range(self.repeats):
#             val = self.func(*args, **kwargs)
#         return val


def do_twice(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper


# Sample Input 1:
@do_twice
def beegeek():
    print('beegeek')


beegeek()

# Sample Output 1:
# beegeek
# beegeek

# Sample Input 2:
@do_twice
def beegeek():
    print('beegeek')


print(beegeek())

# Sample Output 2:
# beegeek
# beegeek
# None
