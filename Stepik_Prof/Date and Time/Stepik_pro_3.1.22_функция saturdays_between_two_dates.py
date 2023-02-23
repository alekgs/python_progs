"""
Функция saturdays_between_two_dates()

Реализуйте функцию saturdays_between_two_dates(), которая принимает два аргумента в следующем порядке:
    start — начальная дата, тип date
    end — конечная дата, тип date

Функция должна возвращать количество суббот между датами start и end включительно.

Примечание 1.
Даты могут передаваться в любом порядке, то есть не гарантируется, что первая дата меньше второй.
Примечание 2.
В тестирующую систему сдайте программу, содержащую только необходимую функцию saturdays_between_two_dates(),
но не код, вызывающий ее.


Sample Input 1:
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))

Sample Output 1:
3

Sample Input 2:
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))

Sample Output 2:
4

Sample Input 3:
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)
print(saturdays_between_two_dates(date1, date2))

Sample Output 3:
0

"""
from datetime import date


def saturdays_between_two_dates(start: date, end: date) -> int:
    """Возвращает количество суббот между датами start и end включительно"""
    # start, end = min(start, end), max(start, end)
    if start > end:
        start, end = end, start
    return sum(date.fromordinal(d).weekday() == 5 for d in range(start.toordinal(), end.toordinal() + 1))


# Тесты
# 1
date1 = date(2021, 11, 1)
date2 = date(2021, 11, 22)
print(saturdays_between_two_dates(date1, date2))
# 2
date1 = date(2020, 7, 26)
date2 = date(2020, 7, 2)
print(saturdays_between_two_dates(date1, date2))
# 3
date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)
print(saturdays_between_two_dates(date1, date2))
