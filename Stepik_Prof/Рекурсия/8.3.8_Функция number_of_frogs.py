"""
Функция number_of_frogs()

В первый год в пруду живет 77 лягушек. Каждый год из пруда вылавливают 30 лягушек, а оставшиеся размножаются,
и их становится в три раза больше. Так, количество лягушек k-й год  может быть описано формулой:

Fk=3(Fk−1−30)
Fk​=3(Fk−1​−30)

Реализуйте функцию number_of_frogs() с использованием рекурсии, которая принимает один аргумент:

    year — натуральное число

Функция должна возвращать единственное число — количество лягушек в пруду в году year.


Sample Input 1:
print(number_of_frogs(2))

Sample Output 1:
141

Sample Input 2:
print(number_of_frogs(10))

Sample Output 2:
629901

Sample Input 3:
print(number_of_frogs(1))

Sample Output 3:
77
"""


def number_of_frogs(year):
    if year == 1:
        return 77
    return 3 * (number_of_frogs(year - 1) - 30)


print(number_of_frogs(1))
