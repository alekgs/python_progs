"""
Итератор Repeater

Реализуйте класс Repeater, порождающий итераторы, конструктор которого принимает один аргумент:
    obj — произвольный объект

Итератор класса Repeater должен бесконечно генерировать единственное значение — obj.
"""


class Repeater:
    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        return self.obj


# Sample Input 1:
bee = Repeater('bee')
print(next(bee))

# Sample Output 1:
# bee

# Sample Input 2:
geek = Repeater('geek')
print(next(geek))
print(next(geek))
print(next(geek))

# Sample Output 2:
# geek
# geek
# geek
