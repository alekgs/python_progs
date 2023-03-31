"""
Функция is_prime()
Реализуйте функцию is_prime() с использованием генераторных выражений, которая принимает один аргумент:
    number — натуральное число

Функция должна возвращать True, если число number является простым, или False в противном случае.

Примечание 1.
Простое число — натуральное число, имеющее ровно два различных натуральных делителя — единицу и самого себя.

Примечание 2.
В задаче удобно воспользоваться функциями all() или any().

"""


def is_prime(n):
    if n == 1:
        return False
    return all(n % d for d in range(2, int(n ** 0.5) + 1))


# def is_prime(n):
#     if n != 1:
#         return all(n % i for i in range(2, n))
#     return False


# Sample Input 1:
print(is_prime(7))

# Sample Output 1:
# True

# Sample Input 2:
print(is_prime(8))

# Sample Output 2:
# False

# Sample Input 3:
print(is_prime(1))

# Sample Output 3:
# False

# TEST_4:
print(is_prime(16))
# False

# TEST_5:
print(is_prime(27))
# False

# TEST_6:
print(is_prime(13))
# True

# TEST_7:
print(is_prime(421))
# True

# TEST_8:
print(is_prime(1061))
# True

# TEST_9:
print(is_prime(9973))
# True
