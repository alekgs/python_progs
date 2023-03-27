"""
Функция print_digits() 😉

Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
    number — натуральное число

Функция должна выводить все цифры числа number, начиная с младших разрядов, каждое на отдельной строке.

Sample Input 1:
print_digits(12345)

Sample Output 1:
5
4
3
2
1

Sample Input 2:
print_digits(7)

Sample Output 2:
7
"""


def print_digits(n):
    if n:
        print(n % 10)
        if n >= 10:
            print_digits(n // 10)


print_digits(9)
