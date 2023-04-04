"""
Функция tabulate()

Реализуйте функцию tabulate(), которая принимает один аргумент:
    func — произвольная функция

Функция tabulate() должна возвращать итератор, генерирующий бесконечную последовательность
возвращаемых значений функции func сначала с аргументом 1, затем 2, затем 3, и так далее.
"""
from itertools import count


def tabulate(func):
    # 1
    # for i in count(1):
    #     yield func(i)

    # 2
    # return (func(i) for i in count(1))

    # 3
    return map(func, count(1))


# Sample Input 1:

func = lambda x: x
values = tabulate(func)
print(next(values))
print(next(values))

# Sample Output 1:
# 1
# 2

# Sample Input 2:
func = lambda x: x + 10
values = tabulate(func)
print(next(values))
print(next(values))
print(next(values))

# Sample Output 2:
# 11
# 12
# 13
