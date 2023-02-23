"""
Функция get_date_range()

Реализуйте функцию get_date_range(), которая принимает два аргумента в следующем порядке:
    start — начальная дата, тип date
    end — конечная дата, тип date

Функция get_date_range() должна возвращать список, состоящий из дат (тип date) от start до end включительно.
Если start > end, функция должна вернуть пустой список.

Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_date_range(),
но не код, вызывающий ее.

Примечание 2. Тестовые данные доступны по ссылке.

Sample Input 1:
date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)

print(*get_date_range(date1, date2), sep='\n')

Sample Output 1:
2021-10-01
2021-10-02
2021-10-03
2021-10-04
2021-10-05

Sample Input 2:
date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))

Sample Output 2:
[datetime.date(2019, 6, 5)]

"""
from datetime import date, timedelta


def get_date_range(start, end):
    return [date.fromordinal(i) for i in range(start.toordinal(), end.toordinal() + 1)]
#
# def get_date_range(d1: date, d2: date) -> list:
#     """Возвращает список, состоящий из дат (тип date) от start до end включительно"""
#     list_date = []
#     delta = d2 - d1
#     if delta.days >= 0:
#         for n in range(delta.days + 1):
#             list_date.append(d1 + timedelta(n))
#     return list_date


# Тесты

date1 = date(2021, 10, 1)
date2 = date(2021, 10, 5)
print(*get_date_range(date1, date2), sep='\n')

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)
print(get_date_range(date1, date2))

