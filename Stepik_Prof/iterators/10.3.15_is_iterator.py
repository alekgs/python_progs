"""
Функция is_iterator()

Реализуйте функцию is_iterator(), которая принимает один аргумент:
    obj — произвольный объект

Функция должна возвращать True, если объект obj является итератором, или False в противном случае.
"""

# is_iterator = lambda obj: hasattr(obj, '__next__')
is_iterator = lambda obj: '__next__' in dir(obj)

# Sample Input 1:
print(is_iterator([1, 2, 3, 4, 5]))

# Sample Output 1:
# False

# Sample Input 2:
beegeek = map(str.upper, 'beegeek')
print(is_iterator(beegeek))

# Sample Output 2:
# True

# Sample Input 3:
beegeek = filter(None, [0, 0, 1, 1, 0, 1])
print(is_iterator(beegeek))

# Sample Output 3:
# True
