"""
Функция get_biggest() 🌶️🌶️

Реализуйте функцию get_biggest(), которая принимает один аргумент:
    numbers — список целых неотрицательных чисел

Функция должна возвращать наибольшее число, которое можно составить из чисел из списка numbers.
Если список numbers пуст, функция должна вернуть число −1−1.

Примечание 1. Рассмотрим первый тест со списком чисел [1, 2, 3], из которых можно составить следующие числа:
123,132,213,231,312,321
123,132,213,231,312,321 Наибольшим из представленных является 321321.

Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_biggest(), но не код,
вызывающий ее.


Sample Input 1:
print(get_biggest([1, 2, 3]))

Sample Output 1:
321

Sample Input 2:
print(get_biggest([61, 228, 9, 3, 11]))

Sample Output 2:
961322811

Sample Input 3:
print(get_biggest([7, 71, 72]))

Sample Output 3:
77271

Sample Input 4:
print(get_biggest([]))

Sample Output 4:
-1


1 находим длину самого длинного числа в списке
2 сортируем список, по убыванию, через ключ str(x) * на 1 пункт
3 склеиваем все элементы списка
4 выводим как число

"""


# Решение № 1
def get_biggest(lst: list) -> int:
    """Возвращает наибольшее число, которое можно составить из чисел из списка numbers"""
    max_num = -1
    if lst:
        max_len = len(str(max(lst)))
        max_num = int(''.join(map(str, sorted(lst, key=lambda x: str(x) * max_len, reverse=True))))
    return max_num


# Решение № 2 - bubble сортировка
# def get_biggest(numbers):
#     if not numbers:
#         return -1
#
#     li = [str(i) for i in numbers]
#     lenght = len(li)
#
#     for i in range(lenght):
#         index = i
#         for j in range(i + 1, lenght):
#             if li[j] + li[index] > li[index] + li[j]:
#                 index = j
#         li[i], li[index] = li[index], li[i]
#
#     return int(''.join(li))

#  Решение № 3  - перестановки через itertools (медленно, не проходит тесты по времени)
# import itertools


# def get_biggest(lst: list) -> int:
#     """Возвращает наибольшее число, которое можно составить из чисел из списка numbers"""
#     if lst:
#         per = itertools.permutations(lst)
#         return max([int(''.join(map(str, list(k)))) for k in per])
#     return -1


# тесты
print(get_biggest([1, 2, 3]))
print(get_biggest([61, 228, 9, 3, 11]))
print(get_biggest([7, 71, 72]))
print(get_biggest([]))
print(get_biggest([0, 0, 0, 0, 0, 0]))

