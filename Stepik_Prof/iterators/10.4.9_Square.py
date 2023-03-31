"""
Итератор Square

Реализуйте класс Square, порождающий итераторы, конструктор которого принимает один аргумент:
    n — натуральное число,

Итератор класса Square должен генерировать последовательность из n чисел, каждое из которых
является квадратом очередного натурального числа, а затем возбуждать исключение StopIteration.
"""


class Square:
    def __new__(cls, n):
        return (i * i for i in range(1, n + 1))


# class Square:
#     def __init__(self, n):
#         self.size = n
#         self.num = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.num == self.size:
#             raise StopIteration
#         self.num += 1
#         return self.num ** 2
#

# Sample Input 1:
squares = Square(2)
print(next(squares))
print(next(squares))

# Sample Output 1:
#
# 1
# 4

# Sample Input 2:
squares = Square(10)
print(list(squares))

# Sample Output 2:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Sample Input 3:
squares = Square(1)
print(list(squares))

# Sample Output 3:
# [1]
