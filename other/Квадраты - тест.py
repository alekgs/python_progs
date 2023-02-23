"""
    Basic timeit framework to test code snippets by Alex Glozman
    Version:  1.6
    Modified: 27.10.2022
"""

import timeit


def run_test(test, setup, repetitions, comment="", precition=6, vars={}, cnt=[0]):
    cnt[0] += 1
    elapsed_time = timeit.timeit(test, setup, number=repetitions, globals=vars)
    print(f'test #{cnt[0]}, elapsed time: {elapsed_time:.{precition}f}, "{comment}" ({repetitions:_} прогонов)')


REPETITIONS = 100_000

test_setup = '''
n = 100_000
'''

test1 = '''
i = 1
while i ** 2  <= n:
    output = i ** 2
    i += 1
'''

test2 = '''
q, odd_sm = 1, 1
while q <= n:
    output = q
    odd_sm += 2
    q += odd_sm
'''

test3 = '''
i, q = 1, 1
while q <= n:
    otput = q
    i += 1
    q = i ** 2
'''

test4 = '''
i = 1
while i * i  <= n:
    output = i * i
    i += 1
'''

test5 = '''
i, q = 1, 1
while q <= n:
    output = q
    i += 1
    q = i * i
'''
test6 = '''
k = 1
n_kv = int(n ** 0.5 // 1)
while k <= n_kv:
    output = k * k
    k += 1
'''

run_test(test1, test_setup, REPETITIONS, "решение с возведением в квадрат")
run_test(test2, test_setup, REPETITIONS, "решение с суммированием нечентых чисел")
run_test(test3, test_setup, REPETITIONS, "оптимизированное решение с возведением в квадрат")
run_test(test4, test_setup, REPETITIONS, "решение с умножением вместо возведением в квадрат")
run_test(test5, test_setup, REPETITIONS, "оптимизированное решение с умножением вместо возведения в квадрат")
run_test(test6, test_setup, REPETITIONS, "Моё решение")
