"""
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму.
В этом треугольнике на вершине и по бокам стоят единицы. Каждое число равно сумме двух расположенных над ним чисел.

На вход программе подается число nn. Напишите программу, которая возвращает указанную строку
треугольника Паскаля в виде списка (нумерация строк начинается с нуля).

"""
import time


# Вариант 1
'''
def pascal(num_str):
    s = []
    for i in range(num_str + 1):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != i and j != 0:
                row[j] = s[i - 1][j - 1] + s[i - 1][j]
        s.append(row)

    return s[num_str] if num_str != 0 else [1]


n = int(input())
start_time = time.time()
print(*pascal(n))
print("--- %s seconds ---" % (time.time() - start_time))
'''

# Вариант 2
from math import factorial as fac


def pascal(n):
    result = []
    for i in range(n + 1):
        result.append((fac(n) // (fac(i) * fac(n - i))))
    return result


k = int(input())
start_time = time.time()
print(*pascal(k))
print("--- %s seconds ---" % (time.time() - start_time))

# Вариант 3
'''
p = [1]
for x in range(int(input())):
    print(*p)
    p[1:] = list(map(lambda a, b: a + b, p, p[1:] + [0]))
'''