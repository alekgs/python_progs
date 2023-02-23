"""
Ваша задача создать функцию-замыкание create_accumulator, она должна накапливать(суммировать) в себе все значения,
которые ей будут переданы, при создании сумма должна быть равна нулю. Посмотрите пример ниже:

summator_1 = create_accumulator()
print(summator_1(1)) # печатает 1
print(summator_1(5)) # печатает 6
print(summator_1(2)) # печатает 8

summator_2 = create_accumulator()
print(summator_2(3)) # печатает 3
print(summator_2(4)) # печатает 7

При каждом вызове должна возвращаться накопленная сумма, которая хранится в замыкании.

Обратите внимание, что объекты из примера summator_1 и summator_2 хранят и накапливают свои собственные суммы.
"""


# через классы
class create_accumulator:
    total = 0

    def __call__(self, value):
        self.total += value
        return self.total


# def create_accumulator():
#     n = 0
#
#     def add(x):
#         nonlocal n
#         n += x
#         return n
#
#     return add


summator_1 = create_accumulator()
print(summator_1(1))  # печатает 1
print(summator_1(5))  # печатает 6
print(summator_1(2))  # печатает 8
print()
summator_2 = create_accumulator()
print(summator_2(3))  # печатает 3
print(summator_2(4))  # печатает 7
