"""
Функция is_power()

Реализуйте функцию is_power() с использованием рекурсии, которая принимает один аргумент:
    number — натуральное число

Функция должна возвращать значение True, если number является степенью числа 2, или False в противном случае.

Sample Input 1:
print(is_power(512))

Sample Output 1:
True

Sample Input 2:
print(is_power(15))

Sample Output 2:
False

Sample Input 3:
print(is_power(1))

Sample Output 3:
True
"""


# def is_power(number):
#     if number == 1:
#         return True
#     if number % 2:
#         return False
#     return is_power(number // 2)

def is_power(number):
    if number % 2:
        return number == 1
    return is_power(number // 2)


print(is_power(512))
print(is_power(15))
print(is_power(1))
