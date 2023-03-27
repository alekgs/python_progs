"""
Функция recursive_sum()

Реализуйте recursive_sum() с использованием рекурсии, которая принимает один аргумент:

    nested_lists — список, элементами которого являются целые числа или списки, элементами которых, в свою очередь,
    также являются либо целые числа, либо списки; вложенность может быть произвольной

Функция должна вычислять сумму всех чисел во всех списках и возвращать полученный результат.
Если список nested_lists пуст, функция должна вернуть число 0.


Sample Input 1:
my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))

Sample Output 1:
24

Sample Input 2:
my_list = []
print(recursive_sum(my_list))

Sample Output 2:
0
"""


def recursive_sum(lst, total=0):
    if not lst:
        return 0

    for i in lst:
        total += i if type(i) is int else recursive_sum(i)
    #
    #     if type(i) is int:
    #         total += i
    #     else:
    #         total += recursive_sum(i)
    return total


my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))

my_list = []
print(recursive_sum(my_list))
