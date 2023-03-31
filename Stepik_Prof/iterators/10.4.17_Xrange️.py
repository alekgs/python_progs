"""
Итератор Xrange 🌶️

Реализуйте класс Xrange, порождающий итераторы, конструктор которого принимает три аргумента
в следующем порядке:
    start — целое или вещественное число
    end — целое или вещественное число
    step — целое или вещественное число, по умолчанию имеет значение 1

Итератор класса Xrange должен генерировать последовательность членов арифметической прогрессии
от start до end, включая start и не включая end, с шагом step, а затем возбуждать исключение
StopIteration.
"""


class Xrange:
    def __init__(self, start, end, step=1):
        self.step = step
        self.end = end
        self.start = start - step

    def __iter__(self):
        return self

    def __next__(self):
        self.start += self.step
        if self.start * self.step >= self.end * self.step:
            raise StopIteration
        return self.start


# class Xrange:
#     def __new__(cls, start, end, step=1):
#         def gen(start):
#             while step * (start - end) < 0:
#                 yield start
#                 start += step
#
#         return gen(start + step - step)


# import numpy
#
#
# class Xrange:
#     def __init__(self, start, end, step=1):
#         self.rng = iter(numpy.arange(start, end, step))
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.rng)


# Sample Input 1:
evens = Xrange(0, 11, 2)
print(*evens)

# Sample Output 1:
# 0 2 4 6 8

# Sample Input 2:
xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')

# Sample Output 2:
# 0.0; 0.5; 1.0; 1.5; 2.0; 2.5

# Sample Input 3:
xrange = Xrange(10, 1, -1)
print(*xrange)

# Sample Output 3:
# 10 9 8 7 6 5 4 3 2

# Sample Input 4:
xrange = Xrange(5, 10)
print(*xrange)

# Sample Output 4:
# 5 6 7 8 9
