"""
Итератор Cycle

Реализуйте класс Cycle, порождающий итераторы, конструктор которого принимает один аргумент:
    iterable — итерируемый объект

Итератор класса Cycle должен циклично генерировать последовательность элементов итерируемого
объекта iterable.

Примечание 1.
Гарантируется, что итерируемый объект, передаваемый в конструктор класса,
не является множеством и итератором.

Примечание 2.
Элементы итерируемого объекта, генерируемые итератором, должны располагаться в
своем изначальном порядке.
"""


class Cycle:
    def __init__(self, iter_obj):
        self.obj = iter_obj
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.obj):
            self.index = 0
        return self.obj[self.index]


# Sample Input 1:
cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

# Sample Output 1:
# b
# e
# b
# e

# Sample Input 2:
cycle = Cycle([1])
print(next(cycle) + next(cycle) + next(cycle))

# Sample Output 2:
# 3

# Sample Input 3:

cycle = Cycle(range(100_000_000))
print(next(cycle))
print(next(cycle))

# Sample Output 3:
# 0
# 1
