"""
Функция flatten()

Реализуйте генераторную функцию flatten(), которая принимает один аргумент: nested_list — список,
элементами которого являются целые числа или списки, элементами которых, в свою очередь,
также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна возвращать генератор, порождающий все числа, содержащиеся в nested_list,
включая все числа из всех вложенных списков, а затем возбуждает исключение StopIteration.
"""


# def flatten(lst):
#     if not lst:
#         return []
#     if isinstance(lst[0], list):
#         return flatten(lst[0]) + flatten(lst[1:])
#     return lst[:1] + flatten(lst[1:])


# def flatten(nested_list):
#     for i in nested_list:
#         yield from flatten(i) if isinstance(i, list) else [i]


def flatten(nested_list):
    for i in nested_list:
        if isinstance(i, list):
            yield from flatten(i)
        else:
            yield i


# Sample Input 1:
generator = flatten([[1, 2], [[3]], [[4], 5]])
print(*generator)

# Sample Output 1:
# 1 2 3 4 5

# Sample Input 2:
generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)

# Sample Output 2:
# 1 2 3 4 5 6 7
