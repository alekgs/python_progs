"""
Функция around()

Реализуйте генераторную функцию, которая принимает один аргумент:
    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность кортежей, каждый из которых
содержит очередной элемент итерируемого объекта iterable, а также предыдущий и следующий за ним
элементы:

(<предыдущий элемент>, <очередной элемент>, <следующий элемент>)

Для первого элемента предыдущим считается значение None, для последнего элемента следующим
считается так же значение None.
"""


def around(iterable):
    if iterable:
        it = iter(iterable)
        flag = None
        j = next(it)
        for i in it:
            yield flag, j, i
            flag = j
            j = i
        yield flag, j, None




# Sample Input 1:
numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

# Sample Output 1:
# (None, 1, 2) (1, 2, 3) (2, 3, 4) (3, 4, 5) (4, 5, None)

# Sample Input 2:
iterator = iter('hey')
print(*around(iterator))

# Sample Output 2:
# (None, 'h', 'e') ('h', 'e', 'y') ('e', 'y', None)
