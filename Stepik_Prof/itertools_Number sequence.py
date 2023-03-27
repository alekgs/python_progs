"""
Напишите программу, которая выводит n первых элементов последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно).

Формат ввода:
Строка, содержащая одно целое число n, n>0.

Формат вывода:
Строка, содержащая требуемую последовательность чисел, разделённых пробелом.

Sample Input:
7

Sample Output:
1 2 2 3 3 3 4

"""
# n = int(input())
# if n == 1:
#     print('1')
# else:
#     s = []
#     for i in range(1, n + 1):
#         s.extend(list(str(i) * i))
#         if len(''.join(s)) > n:
#             break
#     print(*s[:n - len(s)])

# from itertools import count, islice
#
#
# def generate():
#     for i in count(1):
#         yield from [str(i)] * i
#
#
# print(*islice(generate(), int(input())))

# получение значение последовательности по его индексу (от 1 и далее) без подсчёта предыдущих значений
#
ind = int(input())
s = 0
for i in range(1, ind + 1):
    s += i
    if s >= ind:
        print(i)
        break
