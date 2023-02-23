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


def exchange(list1: list, list2: list):
    # копия списка list1
    list_tmp = list(list1)
    # очистка списка 1
    del list1[:]
    list1.extend(list2)
    # очистка списка 2
    del list2[:]
    list2.extend(list_tmp)

    # Метод 2
    # list_tmp = list1.copy()
    #
    # list1.clear()
    # list1.extend(list2)
    #
    # list2.clear()
    # list2.extend(list_tmp)


s1 = ['a', 'b', 'c', 'd']
s2 = ['A', 'V']

exchange(s1, s2)

print(s1)
print(s2)
