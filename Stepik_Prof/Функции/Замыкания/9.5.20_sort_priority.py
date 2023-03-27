"""
Функция sort_priority() 🌶️

Реализуйте функцию sort_priority(), которая принимает два аргумента в следующем порядке:

    values — список чисел
    group — список, кортеж или множество чисел

Функция должна сортировать по неубыванию список чисел values, делая при этом приоритетной группу
чисел из group, которая должна следовать первой.

Отсортировал values, убрал из group все значения которых нет в values.
Отсортировал group.
Энумерировал group.
В цикле по group удалял значение из values и вставлял его же по индексу
(он у нас в энумерации) обратно в values.
"""


# def sort_priority(values, group):
#     b = set(values).difference(set(group))
#     a = set(group) & set(values)
#     values[:] = sorted(a) + sorted(b)
#     return values


def sort_priority(numbers, group):
    numbers.sort(key=lambda x: (x not in group, x))

# с замыканием
# def sort_priority(values, group):
#     values.sort()
#
#     def comparison(x):
#         return x not in group
#     values.sort(key=comparison)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {5, 7, 2, 3}
sort_priority(numbers, group)
print(numbers)
# [2, 3, 5, 7, 1, 4, 6, 8]

numbers = [150, 200, 300, 1000, 50, 20000]
sort_priority(numbers, [300, 100, 200])
print(numbers)
# [200, 300, 50, 150, 1000, 20000]

numbers = [9, 8, 7, 6, 5, 4, 3, 2, 1]
sort_priority(numbers, (300, 100, 200))
print(numbers)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
