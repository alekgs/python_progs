"""
Функция factorials()
Реализуйте функцию factorials() с использованием функции accumulate(), которая принимает один аргумент:
    n — натуральное число

Функция должна возвращать итератор, генерирующий последовательность из n чисел, каждое из которых
является факториалом очередного натурального числа.

"""
# import operator
from itertools import accumulate


def factorials(n):
    # yield from accumulate(range(2, n + 1), operator.mul, initial=1)
    # return accumulate(range(1, n + 1), operator.mul)
    return accumulate(range(1, n + 1), lambda x, y: x * y)

    # 1
    # for i in count(1):
    #     yield func(i)
    # 2
    # return (func(i) for i in count(1))


# Sample Input 1:
numbers = factorials(6)
print(*numbers)

# Sample Output 1:
# 1 2 6 24 120 720

# Sample Input 2:
numbers = factorials(2)
print(next(numbers))
print(next(numbers))

# Sample Output 2:
# 1
# 2
