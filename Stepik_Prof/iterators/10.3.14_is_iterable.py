"""
Функция is_iterable()

Реализуйте функцию is_iterable(), которая принимает один аргумент:
    obj — произвольный объект

Функция должна возвращать True, если объект obj является итерируемым объектом, или False в
противном случае.
"""

is_iterable = lambda obj: hasattr(obj, '__iter__')
# is_iterable = lambda obj: '__iter__' in dir(obj)

# Sample Input 1:
print(is_iterable(18731))

# Sample Output 1:
# False

# Sample Input 2:
print(is_iterable('18731'))

# Sample Output 2:
# True

# Sample Input 3:
objects = [(1, 13), 7.0004, [1, 2, 3]]

for obj in objects:
    print(is_iterable(obj))

# Sample Output 3:
# True
# False
# True
