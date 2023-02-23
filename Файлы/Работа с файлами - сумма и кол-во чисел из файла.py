"""
В этой задаче вам необходимо скачать файл, в котором записаны натуральные числа. Ваша задача найти

    количество трехзначных чисел;
    сумму двухзначных чисел
"""
f = open('numbers.txt')
count_3x, sum_2x = 0, 0
for i in map(int, f.read().splitlines()):
    if i in range(100, 1000):
        count_3x += 1
    elif i in range(10, 100):
        sum_2x += i
print(f'{count_3x},{sum_2x}')

# print(sum(list(map(int, filter(lambda x: len(x) == 2, f.read().splitlines())))))
# f.seek(0)
# print(len(list(map(int, filter(lambda x: len(x) == 3, f.read().splitlines())))))

f.close()
