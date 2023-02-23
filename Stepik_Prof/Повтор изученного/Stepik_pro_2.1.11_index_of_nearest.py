"""
Функция index_of_nearest()

Реализуйте функцию index_of_nearest(), которая принимает два аргумента в следующем порядке:
    numbers — список целых чисел
    number — целое число

Функция должна находить в списке numbers ближайшее по значению число к числу number и возвращать его индекс.
Если список numbers пуст, функция должна вернуть число −1.

Примечание 1.
Если в функцию передается список, содержащий несколько чисел, одновременно являющихся ближайшими к
искомому числу, функция должна возвращать наименьший из индексов ближайших чисел.

Примечание 2.
Рассмотрим третий тест. Ближайшими числами к числу 4 являются 5 и 3, имеющие индексы 1 и 2
соответственно. Наименьший из индексов равен 1.

Sample Input 1:
print(index_of_nearest([], 17))
-1
Sample Input 2:
print(index_of_nearest([7, 13, 3, 5, 18], 0))
2
Sample Input 3:
print(index_of_nearest([9, 5, 3, 2, 11], 4))
1
Sample Input 4:
print(index_of_nearest([7, 5, 4, 4, 3], 4))
2


Решение:

1 если длина списка меньше 1, то возвращаем -1
2 ищем минимальный элемент, из списка numbers, ключ лямбда abs(x-number)
3. возвращаем ИНДЕКС этого элемента, а не сам элемент!!

"""


def index_of_nearest(numbers: list, num: int) -> int:
    """Находит в списке numbers ближайшее по значению число к числу number и возвращать его индекс"""
    if numbers:
        return numbers.index(min(numbers, key=lambda num_lst: abs(num_lst - num)))
    return -1


# тесты
print(index_of_nearest([], 17))  # -1
print(index_of_nearest([7, 13, 3, 5, 18], 0))  # 2
print(index_of_nearest([9, 5, 3, 2, 11], 4))  # 1
print(index_of_nearest([7, 5, 4, 4, 3], 4))  # 2
print(index_of_nearest([6, 100, 101, 2], 4))  # 0
print(index_of_nearest([734234423423423, 5343423423546463423, 934234423423423423, -1], 0))  # 3
print(index_of_nearest([1, 14, 100, 65, 6], 5))  # 4
print(index_of_nearest([10, 164, 100, 265, 16], 8))  # 0
print(index_of_nearest([10, 99, 0, -12, 16], -9))  # 3
print(index_of_nearest([1, 1, 1, 1, 1], 1))  # 0
