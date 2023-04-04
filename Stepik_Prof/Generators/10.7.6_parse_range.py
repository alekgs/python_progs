"""
Функция parse_ranges()

Назовем диапазоном запись двух натуральных чисел через дефис a-b, где a — левая граница
диапазона, b — правая граница диапазона, причем a <= b. Диапазон содержит в себе все числа от a
до b включительно. Например, диапазон 1-4 содержит числа 1, 2, 3 и 4.

Реализуйте генераторную функцию parse_ranges(), которая принимает один аргумент:
    ranges — строка, в которой через запятую указаны диапазоны чисел

Функция должна возвращать генератор, порождающий последовательность чисел, содержащихся в
диапазонах ranges.
"""


def parse_ranges(ranges):
    for a, b in (r.split('-') for r in ranges.split(',')):
        yield from range(int(a), int(b) + 1)


# def parse_ranges(ranges: str):
#     for r in ranges.split(','):
#         start, end = map(int, r.split('-'))
#         yield from range(start, end + 1)

# def parse_ranges(ranges):
#     return (j
#             for i in ranges.split(',')
#             for a, b in [i.split('-')]
#             for j in range(int(a), int(b) + 1))


# def parse_ranges(ranges: str):
#     chain1 = (s for s in ranges.split(','))
#     chain2 = (s.split('-') for s in chain1)
#     chain3 = (map(int, s) for s in chain2)
#     return (i for a, b in chain3 for i in range(a, b + 1))


# Sample Input 1:
print(*parse_ranges('1-2,4-4,8-10'))

# Sample Output 1:
# 1 2 4 8 9 10

# Sample Input 2:
print(*parse_ranges('1-10,2-10'))

# Sample Output 2:
# 1 2 3 4 5 6 7 8 9 10 2 3 4 5 6 7 8 9 10

# Sample Input 3:
print(*parse_ranges('7-32'))

# Sample Output 3:
# 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
