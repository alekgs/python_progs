"""
Функция custom_sort() 🌶️

Реализуйте функцию custom_sort(), которая принимает два аргумента в следующем порядке:
    ordered_dict — словарь OrderedDict
    by_values — булево значение, по умолчанию имеет значение False

Функция должна сортировать словарь ordered_dict:
- по ключам, если by_values имеет значение False
 - по значениям, если by_values имеет значение True

Примечание 1.
Функция должна изменять переданный словарь, а не возвращать новый.
Возвращаемым значением функции должно быть None.

Примечание 2.
Гарантируется, что переданный в функцию словарь можно отсортировать, то есть он не содержит ключи,
имеющие разные типы, а также значения, имеющие разные типы.

Примечание 3.
Если два элемента имеют равные значения, то следует сохранить их исходный порядок следования.
"""
from collections import OrderedDict

# 1
# def custom_sort(ordered_dict, by_values=False) -> None:
#     if by_values:
#         d = OrderedDict(sorted(ordered_dict.items(), key=lambda x: x[1]))
#     else:
#         d = OrderedDict(sorted(ordered_dict.items()))
#     for key in d:
#         ordered_dict.move_to_end(key)


# 2
def custom_sort(dat, by_values=False):
    for key in sorted(dat, key=(None, dat.get)[by_values]):
        dat.move_to_end(key)


# 3
# def custom_sort(data, by_values=False):
#     if by_values:
#         for key in sorted(data, key=lambda k: data[k]):
#             data.move_to_end(key)
#     else:
#         for key in sorted(data):
#             data.move_to_end(key)


# 1
data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
custom_sort(data)
print(data)

# Sample Output 1:
# OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])

# 2
data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())

# Sample Output 2:
# ('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)
