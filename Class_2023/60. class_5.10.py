"""
Требуется написать функцию 'count_less8', которая на вход принимает список из n целых чисел
и возвращает количество чисел, в записи которых нет цифры 8.
Пример

Ввод
1 2 3 4 5 6 7 8 9 0

Вывод
9
"""


def count_less8(n):
    count = 0
    a = n.split()
    for i in a:
        if int(i) % 10 != 8:
            count += 1
    return count

print(count_less8([1,2,3,4,5,6,7,8,9,0]))