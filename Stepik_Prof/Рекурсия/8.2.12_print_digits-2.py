"""
Функция print_digits() 😉

Реализуйте функцию print_digits() с использованием рекурсии, которая принимает один аргумент:
    number — натуральное число

Функция должна выводить все цифры числа number, начиная со старших разрядов, каждое на отдельной строке.

Sample Input 1:
print_digits(12345)

Sample Output 1:
1
2
3
4
5

Sample Input 2:
print_digits(2077)

Sample Output 2:
2
0
7
7

Sample Input 3:
print_digits(8)

Sample Output 3:
8
"""


def print_digits(n):
    if n > 9:
        print_digits(n // 10)
    print(n % 10)


print_digits(12345)
