"""
Функция tribonacci()

Последовательность Трибоначчи – последовательность натуральных чисел, где каждое последующее число является
суммой трех предыдущих: 1,1, 1, 3, 5, 9, 17, 31, 57, 105 …


Реализуйте функцию tribonacci() с использованием рекурсии и мемоизации, которая принимает один аргумент:
    n — натуральное число

Функция должна возвращать n-й член последовательности Трибоначчи.

Sample Input 1:
print(tribonacci(1))

Sample Output 1:
1

Sample Input 2:
print(tribonacci(7))

Sample Output 2:
17

Sample Input 3:
print(tribonacci(4))

Sample Output 3:
3
"""


from functools import lru_cache


@lru_cache
def tribonacci(x):
    if x in [1, 2, 3]:
        return 1
    return tribonacci(x - 3) + tribonacci(x - 1) + tribonacci(x - 2)

# def tribonacci(n, f1=1, f2=1, f3=1) -> int:
#     if n == 1:
#         return f1
#     return tribonacci(n - 1, f2, f3, f1 + f2 + f3)


# def tribonacci(n):
#     cache = {1: 1, 2: 1, 3: 1}
#
#     def fib_rec(num):
#         result = cache.get(num)
#         if result is None:
#             result = fib_rec(num - 3) + fib_rec(num - 2) + fib_rec(num - 1)
#             cache[num] = result
#         return result
#
#     return fib_rec(n)


print(tribonacci(1))
print(tribonacci(7))
print(tribonacci(1500))
