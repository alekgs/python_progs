"""
Итератор Fibonacci

Реализуйте класс Fibonacci, порождающий итераторы, конструктор которого не принимает никаких
аргументов. Итератор класса Fibonacci должен генерировать бесконечную последовательность чисел
Фибоначчи, начиная с 1.

Примечание 1. Последовательность Фибоначчи – последовательность натуральных чисел, где каждое
последующее число является суммой двух предыдущих: 1,1,2,3,5,8,13,21,34
"""
# from functools import lru_cache


# class Fibonacci:
#     def __init__(self):
#         self.x = 0
#
#     @lru_cache
#     def fib(self, n):
#         if n <= 2:
#             return 1
#         else:
#             return self.fib(n - 1) + self.fib(n - 2)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.x += 1
#         return self.fib(self.x)


class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


# Sample Input 1:
fibonacci = Fibonacci()
print(next(fibonacci))

# Sample Output 1:
# 1

# Sample Input 2:
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))

# Sample Output 2:
# 1
# 1
# 2
# 3
