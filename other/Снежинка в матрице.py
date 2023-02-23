n = int(input('Введите размер квадратной матрицы: '))
m = [['.'] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == n // 2 or j == n // 2 or i == j or i == n - 1 - j:
            m[i][j] = '*'

[print(*i) for i in m]
