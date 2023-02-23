"""
Функция get_the_fastest_func()

Реализуйте функцию get_the_fastest_func(), которая принимает два аргумента в следующем порядке:
    funcs — список произвольных функций
    arg — произвольный объект

Функция get_the_fastest_func() должна возвращать функцию из списка funcs, которая затратила
на вычисление значения при вызове с аргументом arg наименьшее количество времени.
"""
# from math import factorial
import time


def calculate_it(func, arg):
    t1 = time.perf_counter()
    func(arg)
    return time.perf_counter() - t1


def get_the_fastest_func(funcs: list, arg):  # -> str:
    d = {f.__name__: calculate_it(f, arg) for f in funcs}
    # return min(d, key=d.get)
    return d


# Тесты

#
# def add(arg):
#     time.sleep(0.5)
#     return
#
#
# def slow(arg):
#     time.sleep(0.3)
#
#
# def fast(arg):
#     time.sleep(0.1)
#
#
# def very_fast(arg):
#     time.sleep(0.01)

# def factorial_recurrent(n):                  # рекурсивная функция
#     if n == 0:
#         return 1
#     return n * factorial_recurrent(n - 1)
#
#
# def factorial_classic(n):                    # итеративная функция
#     f = 1
#     for i in range(2, n + 1):
#         f *= i
#     return f
#
#
# def for_and_append(iterations):  # с использованием цикла for и метода append()
#     result = []
#     for i in range(iterations):
#         result.append(i + 1)
#     return result
#
#
# def list_comprehension(iterations):  # с использованием списочного выражения
#     return [i + 1 for i in range(iterations)]

def for_and_append(iterable):  # с использованием цикла for и метода append()
    result = []
    for elem in iterable:
        result.append(elem)
    return result


def list_comprehension(iterable):  # с использованием списочного выражения
    return [elem for elem in iterable]


def list_function(iterable):  # с использованием встроенной функции list()
    return list(iterable)


print(get_the_fastest_func([for_and_append, list_comprehension, list_function], range(100_000)))
# print(get_the_fastest_func([for_and_append, list_comprehension], 10_000_000))
# print(get_the_fastest_func([factorial_classic, factorial_recurrent, factorial], 900))
# print(get_the_fastest_func([slow, fast, add, very_fast], 0))
