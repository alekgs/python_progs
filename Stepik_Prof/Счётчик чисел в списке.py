"""
Рассмотрим задачу:
пусть задан список чисел numbers, в котором некоторые числа встречаются несколько раз.
Нужно узнать, сколько именно раз встречается каждое из чисел.
"""
from collections import Counter, defaultdict
numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
words = ['abc', 'bca', 'bca', 'def']
# DefaultDict
# result = defaultdict(int)
# for num in numbers:
#     result[num] += 1
# print(result)

# Counter
print(Counter(numbers))
# print(sorted(Counter(numbers).items()))
print(Counter(words))


