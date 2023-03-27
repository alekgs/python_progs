"""
Функция non_negative_even()

Реализуйте функцию non_negative_even(),  которая принимает один аргумент:

    numbers — непустой список чисел

Функция должна возвращать True, если все числа в списке numbers являются четными и неотрицательными, или False в
противном случае.

Примечание 1. В задаче удобно воспользоваться функцией all().
"""


def non_negative_even(numbers):
    return all(map(lambda x: x >= 0 and not x % 2, numbers))


# Sample Input 1:
print(non_negative_even([0, 2, 4, 8, 16]))

# Sample Output 1:
# True

# Sample Input 2:
print(non_negative_even([-8, -4, -2, 0, 2, 4, 8]))

# Sample Output 2:
# False

# Sample Input 3:
print(non_negative_even([0, 0, 0, 0, 0]))

# Sample Output 3:
# True
