"""
Функция unique()

Реализуйте генераторную функцию, которая принимает один аргумент:
    iterable — итерируемый объект

Функция должна возвращать генератор, порождающий последовательность элементов итерируемого
объекта iterable без дубликатов.

Примечание 1. Элементы итерируемого объекта в возвращаемом функцией генераторе должны
располагаться в своем исходном порядке.

Примечание 2.
Гарантируется, что итерируемый объект, передаваемый в функцию, не является множеством.
"""


# from collections import Counter

def unique(obj):
    yield from (dict.fromkeys(obj))


# def unique(obj):
#    yield from {i: 1 for i in obj}

# yield from Counter(obj)


# Sample Input 1:
numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))

# Sample Output 1:
# 1 2 3 4 5

# Sample Input 2:
iterator = iter('111222333')
uniques = unique(iterator)
print(next(uniques))
print(next(uniques))
print(next(uniques))

# Sample Output 2:
# 1
# 2
# 3

# TEST_3:
data = map(abs, range(-100, 100))
print(*unique(data))

# 100 99 98 97 96 95 94 93 92 91 90 89 88 87 86 85 84 83 82 81 80 79 78 77 76 75 74 73 72
# 71 70 69 68 67 66 65 64 63 62 61 60 59 58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40
# 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 7
# 6 5 4 3 2 1 0


# TEST_4:
data = map(str.upper, 'jhfjgshgkjfdjsgriyteryowpqerkelfsldfmnmnbmvcnmlgqweootiyoeytkldjhmvxcmkasd')
print(*unique(data))
# J H F G S K D R I Y T E O W P Q L M N B V C X A

# TEST_5:
data = 'JSKFJSDIFjejfkdjKJFIOJfkgkSDJGIEJGsklGDnvmmcvlwoqeriwjndSKF'
print(*unique(data))
# J S K F D I j e f k d O g G E s l n v m c w o q r i

# TEST_6:
data = map(str.lower, 'STEPIK')
print(*unique(data))
# s t e p i k

# TEST_7:
data = map(str.lower, 'SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS')
print(*unique(data))
# s

# TEST_8:
data = ['bee', 'geek', 'stepik', 'python']
print(*unique(data))
# bee geek stepik python

# TEST_9:
print(list(unique([])))  # []
