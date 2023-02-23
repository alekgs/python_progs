"""
На вход программе подаются два числа nn и mm — количество строк и столбцов в матрице,
далее идут n×mn×m слов, каждое на отдельной строке.
Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.
"""

#  строки, столбцы
row, col, matrix = int(input('Число строк ?: ')), int(input('Число столбцов ?: ')), []


# Ввод числовой матрицы

# способ 1
# matrix = [[int(i) for i in input().split()] for i in range(n)]
# mult = [[i * j for j in range(m)] for i in range(n)]

# способ 2
# for _ in range(n):
#     row = [int(i) for i in input().split()]
#     matrix.append(row)


# вводим матрицу
for i in range(row):
    # вводим матрицу
    matrix.append([int(input(f'Элемент матрицы [{i}][{j}] : ')) for j in range(col)])


# печатаем матрицу
print()
print(f'Матрица {row}x{col}:')
# for i in range(row):
#     for j in range(col):
#         print(str(matrix[i][j]).rjust(5), end=' ')
#     print()

for k in matrix:
    print(*[str(s).ljust(3) for s in k])


"""
Выводить можно и так на печать
for r in mult:
    print(*[str(c).ljust(2) for c in r])
"""

# печать транспонированной матрицы

# for i in range(n):
#    print(*[matrix[j][i] for j in range(n)])

# for i in range(col):
#     for j in range(row):
#         print(matrix[j][i], end=' ')
#     print()


# способ 2
# n, m = (int(input()) for _ in '12')
# s = [[input() for _ in range(m)] for _ in range(n)]
# [print(*i) for i in s]


# способ 3
# def print_matrix(a):
#     for i in range(len(a)):
#         print(*a[i])
#
#
# rows = int(input())
# cols = int(input())
# a = [[input() for j in range(cols)] for i in range(rows)]
# b = [[a[i][j] for i in range(rows)] for j in range(cols)]
#
# print_matrix(a)
# print()
# print_matrix(b)
