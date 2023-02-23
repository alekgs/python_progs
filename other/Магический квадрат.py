"""
Магический квадрат 🌶️

Магическим квадратом порядка nn называется квадратная таблица размера n×n, составленная
из всех чисел 1,2,3,… n**2 так, что суммы по каждому столбцу, каждой строке и каждой из двух диагоналей равны
между собой. Напишите программу, которая проверяет, является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подаётся натуральное число nn — количество строк и столбцов в матрице,
затем элементы матрицы: nn строк, по nn чисел в каждой, разделённые пробелами.

Формат выходных данных
Программа должна вывести слово YES, если матрица является магическим квадратом, и слово NO в противном случае.
"""
n = int(input())
matrix = [[int(i) for i in input().split()] for j in range(n)]

# магическое число
magic = sum(matrix[0])

flag = 'YES'

# проверка на цифры (1,2,3,... n ** 2)
digits = [i for i in range(1, n ** 2 + 1)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] in digits:
            digits.remove(matrix[i][j])
    if i == n - 1 and j == n - 1 and digits != []:
        flag = 'NO'

# сумма по строкам
for i in range(n):
    if sum(matrix[i]) != magic:
        flag = 'NO'
        break

# сумма по столбцам
for j in range(n):
    result = 0
    for i in range(n):
        result += matrix[i][j]
        if i == n - 1 and result != magic:
            flag = 'NO'
            break

# сумма главной диагонали
result = 0
for i in range(n):
    result += matrix[i][i]
if result != magic:
    flag = 'NO'

# сумма побочной диагонали
result = 0
for i in range(n):
    result += matrix[i][n - i - 1]
if result != magic:
    flag = 'NO'

print(flag)
