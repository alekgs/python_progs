"""
Итератор PowerOf

Реализуйте класс PowerOf, порождающий итераторы, конструктор которого принимает один аргумент:
    number — ненулевое число

Итератор класса PowerOf должен генерировать бесконечную последовательность целых неотрицательных
степеней числа number в порядке возрастания, начиная с нулевой степени.

"""


class PowerOf:
    def __init__(self, n):
        self.num = n
        self.pow = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.pow += 1
        return self.num ** self.pow


# Sample Input:
power_of_two = PowerOf(2)

print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))

# Sample Output:
#
# 1
# 2
# 4
# 8
