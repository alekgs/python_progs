"""
Функция power()

Реализуйте функцию power(), которая принимает один аргумент:
    degree — целое число

Функция power() должна возвращать функцию, которая принимает в качестве аргумента целое число x и
возвращает значение x в степени degree.
Примечание 1.
Рассмотрим пример из первого теста. Вызов power(2) возвращает функцию, которая принимает
в качестве аргумента число и возводит его во вторую степень. Функция присваивается
переменной square. Далее полученная функция вызывается с аргументом 55 и
возвращает значение 52=2552=25.

Sample Input 1:
square = power(2)
print(square(5))

Sample Output 1:
25

Sample Input 2:
print(power(3)(3))

Sample Output 2:
27

Sample Input 3:
result = power(4)(2)
print(result)

Sample Output 3:
16
"""


def power(degree):
    return lambda x: x ** degree


square = power(2)
print(square(5))

print(power(3)(3))

result = power(4)(2)
print(result)
