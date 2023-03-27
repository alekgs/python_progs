"""
Быстрое возведение в степень

Возводить в степень можно гораздо быстрее, чем за n умножений.

Реализуйте функцию get_fast_pow() с использованием рекурсии, которая принимает два аргумента в следующем порядке:
    a — положительное целое число
    n — неотрицательное целое число

Функция должна вычислять значение a в степени n, используя алгоритм быстрого возведения в степень, и возвращать
полученный результат.

Примечание 1.  При решении не используйте оператор возведения в степень **.

Sample Input 1:
print(get_fast_pow(2, 10))

Sample Output 1:
1024

Sample Input 2:
print(get_fast_pow(5, 2))

Sample Output 2:
25

Sample Input 3:
print(get_fast_pow(2, 100))

Sample Output 3:
1267650600228229401496703205376
"""


def get_fast_pow(a, n):
    if n:
        if n % 2:
            return a * get_fast_pow(a, n - 1)
        return get_fast_pow(a * a, n // 2)
    return 1


print(get_fast_pow(2, 0))
print(get_fast_pow(2, 5))
print(get_fast_pow(2, 10))
print(get_fast_pow(5, 3))
print(get_fast_pow(2, 100))
print(get_fast_pow(2, 1000))
