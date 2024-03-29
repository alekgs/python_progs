"""
Минимум и максимум

Напишите программу, которая определяет минимальное и максимальное значения функции на отрезке в целых точках.

Формат входных данных
На вход программе в первой строке подается корректная функция f(x), в следующей строке
вводятся два целых числа a и b, разделенные пробелом, которые представляют границы отрезка [a;b].

Формат выходных данных
Программа должна определить минимальное и максимальное значения функции f(x) на отрезке
[a;b] в целых точках и вывести полученный результат в следующем формате:

Минимальное значение функции <функция f(x)> на отрезке <отрезок> равно <мин. значение>
Максимальное значение функции <функция f(x)> на отрезке <отрезок> равно <макс. значение>

Sample Input 1:
2*x**2 + 5*x + 7
-1 5

Sample Output 1:
Минимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 4
Максимальное значение функции 2*x**2 + 5*x + 7 на отрезке [-1; 5] равно 82

Sample Input 2:
x + 1
-999 999

Sample Output 2:
Минимальное значение функции x + 1 на отрезке [-999; 999] равно -998
Максимальное значение функции x + 1 на отрезке [-999; 999] равно 1000
"""

f = input()
a, b = map(int, input().split())

res = list(map(lambda x: eval(f), range(a, b + 1)))

print(f'Минимальное значение функции {f} на отрезке [{a}; {b}] равно {min(res)}')
print(f'Максимальное значение функции {f} на отрезке [{a}; {b}] равно {max(res)}')


