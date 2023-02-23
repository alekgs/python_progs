"""
На вход программе подается натуральное число nn. Напишите программу, которая выводит
первые nn строк треугольника Паскаля.
Программа должна вывести первые nn строк треугольника Паскаля, каждую на отдельной строке в соответствии с образцом.
"""
import time
from math import factorial as fac


def pascal(n):
    result = []
    for i in range(n + 1):
        result.append((fac(n) // (fac(i) * fac(n - i))))
    return result


nums = int(input('Введите число первых строк треугольника Паскаля: '))
start_time = time.time()
for j in range(nums):
    print(*pascal(j))

print("--- %s seconds ---" % (time.time() - start_time))
