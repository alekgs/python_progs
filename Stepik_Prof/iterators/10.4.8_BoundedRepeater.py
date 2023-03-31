"""
Итератор BoundedRepeater

Реализуйте класс BoundedRepeater, порождающий итераторы, конструктор которого принимает два
аргумента в следующем порядке:

    obj — произвольный объект
    times — натуральное число

Итератор класса BoundedRepeater должен генерировать значение obj times раз, а затем возбуждать
исключение StopIteration.
"""


class BoundedRepeater:
    def __init__(self, obj, times):
        self.obj = obj
        self.times = times

    def __iter__(self):

        return self

    def __next__(self):
        if not self.times:
            raise StopIteration
        self.times -= 1
        return self.obj


# Sample Input 1:

bee = BoundedRepeater('bee', 2)
print(next(bee))
print(next(bee))

# Sample Output 1:
# bee
# bee


# Sample Input 2:
geek = BoundedRepeater('geek', 3)
print(next(geek))
print(next(geek))
print(next(geek))

try:
    print(next(geek))
except StopIteration:
    print('Error')

# Sample Output 2:
# geek
# geek
# geek
# Error
