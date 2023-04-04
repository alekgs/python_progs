"""
Функция years_days()

Реализуйте генераторную функцию years_days(), которая принимает один аргумент:
    year — натуральное число

Функция должна возвращать генератор, порождающий последовательность всех дат (тип date) в году year.

Примечание 1.

Возьмем в качестве примера 2022 год. В январе этого года 31 день, в феврале — 28, в марте — 31,
и так далее. Тогда генератор, полученный при вызове years_days(2022), должен порождать сначала
все даты с 1 по 31 января, затем с 11 по 28 февраля, и так далее до 31 декабря.

"""
# from calendar import Calendar
#
# def years_days(year):
#     return(d for m in range(1, 13) for d in Calendar().itermonthdates(year, m) if d.month == m)

from datetime import date, timedelta


# def years_days(year: int):
#     start = date(year, 1, 1)
#     while start.year == year:
#         yield start
#         start += timedelta(days=1)


from datetime import date


def years_days(year):
    start = date(year, 1, 1).toordinal()
    end = date(year + 1, 1, 1).toordinal()
    yield from (date.fromordinal(i) for i in range(start, end))


# Sample Input:
dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))

# Sample Output:
# 2022-01-01
# 2022-01-02
# 2022-01-03
# 2022-01-04
