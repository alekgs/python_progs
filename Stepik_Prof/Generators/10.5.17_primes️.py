"""
Функция primes()
Реализуйте генераторную функцию primes(), которая принимает два аргумента в следующем порядке:
    left — натуральное число
    right — натуральное число

Функция должна возвращать генератор, порождающий последовательность простых чисел от left до
right включительно, а затем возбуждающий исключение StopIteration.

Примечание 1. Гарантируется, что left <= right.

Примечание 2.
Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу
и самого себя. Единица простым числом не является.
"""


def primes(a, b):
    if a == 1:
        a += 1
    for n in range(a, b + 1):
        for d in range(2, n):
            if not n % d:
                break
        else:
            yield n


# Sample Input 1:
generator = primes(1, 15)
print(*generator)

# Sample Output 1:
# 2 3 5 7 11 13

# Sample Input 2:
generator = primes(6, 36)
print(next(generator))
print(next(generator))

# Sample Output 2:
# 7
# 11
