def get_combin(n: int, k: int) -> int:
    """Принимает на вход два целых числа  и находит
    c(n, k) — число сочетаний из n элементов по k """
    if k == 0 or k == n:
        return 1
    if 0 < k < n:
        return get_combin(n - 1, k) + get_combin(n - 1, k - 1)


print(get_combin(6, 5))
