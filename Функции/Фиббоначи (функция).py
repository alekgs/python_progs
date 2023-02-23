def fibb(n: int) -> int | None:
    """ Функция возвращает значение n-го числа ряда Фиббоначи"""
    if n == 0:
        return 0
    if n == 1:
        return 1
    fib1 = fib2 = 1
    while n - 2 > 0:
        fib1, fib2 = fib2, fib1 + fib2
        n -= 1
    return fib2


print([fibb(i) for i in range(30)])

