"""
Итератор DictItemsIterator

Как известно, во время итерации по словарю мы получаем ключи, а не значения или пары ключ-значение.

Приведенный ниже код:
info = {'name': 'Timur', 'age': 29, 'gender': 'Male'}
print(*info)

выводит:
name age gender

Реализуйте класс DictItemsIterator, порождающий итераторы, конструктор которого принимает один
аргумент: data — словарь

Итератор класса DictItemsIterator должен генерировать последовательность кортежей, представляющих
собой пары ключ-значение словаря data, а затем возбуждать исключение StopIteration.

Примечание 1.
При решении задачи не используйте словарные методы keys(), values() и items().

Примечание 2. Пары ключ-значение в возвращаемом функцией итераторе должны располагаться в своем
изначальном порядке.
"""


# class DictItemsIterator:
#     def __new__(cls, data):
#         return map(lambda key: (key, data[key]), data)

# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#         self.key = iter(data)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         key = next(self.key)
#         return key, self.data[key]


class DictItemsIterator:
    def __init__(self, data: dict):
        self.d = tuple(map(lambda key: (key, data[key]), data))
        self.size = len(data) - 1
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == self.size:
            raise StopIteration
        self.index += 1
        return self.d[self.index]


# Sample Input 1:
pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)

# Sample Output 1:
# (1, 'A') (2, 'B') (3, 'C')

# Sample Input 2:
data = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49}
pairs = DictItemsIterator(data)
print(*pairs)

# Sample Output 2:
# (1, 1) (2, 4) (3, 9) (4, 16) (5, 25) (6, 36) (7, 49)
