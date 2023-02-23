"""
Квадратное уравнение
"""


def discriminant(a: int, b: int, c: int) -> int:
    """
    Функция для нахождения дискриминанта
    """
    return b * b - 4 * a * c


def solution(a: int, b: int, c: int) -> int or None:
    """
    Функция для нахождения корней уравнения
    """
    d = discriminant(a, b, c)
    res = 'корней нет'
    if d < 0:
        res = 'корней нет'
    elif d == 0:
        res = -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        res = f'{min(x1, x2)} {max(x1, x2)}'
    return res


# тесты
print(solution(-1, -2, 15))
print(solution(1, -13, 12))
print(solution(-4, 28, -49))
print(solution(1, 1, 1))


