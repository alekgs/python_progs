"""
Требуется написать функцию exchange(), которая принимает на вход два списка строк и меняет местами их содержимое.
Функция не должна ничего ни возвращать, ни выводить.

Пример
Ввод
Moscow Paris Washington
Russia France USA

Вывод
Russia France USA
Moscow Paris Washington
"""


def exchange(list1, list2):
    ...
    list1, list2 = list2, list1
    return list1, list2


s1 = ['a', 'b', 'c']
s2 = ['A', 'B', 'C']

exchange(s1, s2)

print(s1)
print(s2)
