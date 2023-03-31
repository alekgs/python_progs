"""
Функция random_numbers()

Реализуйте функцию random_numbers(), которая принимает два аргумента:
    left — целое число
    right — целое число

Функция должна возвращать итератор, генерирующий бесконечную последовательность случайных целых
чисел в диапазоне от left до right включительно.

Примечание 1. Гарантируется, что left <= right.
"""
from random import randint


# def random_numbers(left, right):
#     def get_numbers():
#         return randint(left, right)
#     return iter(get_numbers, None)

def random_numbers(start: int, end: int) -> iter:
    return iter(lambda: randint(start, end), None)

# Sample Input 1:
iterator = random_numbers(1, 1)

print(next(iterator))
print(next(iterator))

# Sample Output 1:
# 1
# 1

# Sample Input 2:
iterator = random_numbers(1, 10)

print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))

# Sample Output 2:
# True
# True
# True
