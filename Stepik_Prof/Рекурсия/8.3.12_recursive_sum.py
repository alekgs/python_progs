"""
Функция recursive_sum()

Реализуйте функцию recursive_sum() с использованием рекурсии, которая принимает два аргумента в следующем порядке:

    a — неотрицательное целое число
    b — неотрицательное целое число

Функция должна возвращать сумму чисел a и b. При вычислении суммы функция:

    не должна использовать циклы
    из всех арифметических операций должна использовать только +1 и −1

Sample Input 1:
print(recursive_sum(10, 22))

Sample Output 1:
32

Sample Input 2:
print(recursive_sum(99, 0))

Sample Output 2:
99

Sample Input 3:
print(recursive_sum(0, 0))

Sample Output 3:
0


"""


def recursive_sum(a, b):
    if b:
        return recursive_sum(a + 1, b - 1)
    return a


print(recursive_sum(10, 22))
print(recursive_sum(99, 0))
print(recursive_sum(0, 0))
