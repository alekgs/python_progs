"""
Функция is_greater()

Реализуйте функцию is_greater(), которая принимает два аргумента в следующем порядке:

    lists — список, элементами которого являются списки целых чисел
    number — целое число

Функция должна возвращать True, если хотя бы в одном вложенном списке из списка lists сумма всех элементов больше
number, или False в противном случае.

Примечание 1. В задаче удобно воспользоваться функцией any().
"""


def is_greater(lists, number):
    return any(map(lambda x: sum(x) > number, lists))


# Sample Input 1:
data = [[-3, 4, 0, 1], [1, 1, -4], [0, 0], [9, 3]]
print(is_greater(data, 10))

# Sample Output 1:
# True

# Sample Input 2:
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]
print(is_greater(data, 2))

# Sample Output 2:
# False

# Sample Input 3:
data = [[0, 1, 2], [0, 3], [1, 1, 1], [3]]
print(is_greater(data, 3))

# Sample Output 3:
# False


