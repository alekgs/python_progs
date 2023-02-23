"""
Функция get_min_max()

Реализуйте функцию get_min_max(), которая принимает один аргумент:
    dates — список дат (тип date)

Функция должна возвращать кортеж, первым элементом которого является минимальная дата из списка dates,
вторым — максимальная дата из списка dates. Если список dates пуст, функция должна вернуть пустой кортеж.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_min_max(), но не код,
вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))

Sample Output 1:
print(get_min_max((datetime.date(1992, 6, 10), datetime.date(2021, 10, 5))

Sample Input 2:
print(get_min_max([]))
Sample Output 2:
()
"""
from datetime import date


def get_min_max(l_dates: list) -> tuple:
    res = ()
    if l_dates:
        res = (min(l_dates), max(l_dates))
    return res


# Тесты
dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
print(get_min_max(dates))
print(get_min_max([]))
