"""
Функция num_of_sundays()

Реализуйте функцию num_of_sundays(), которая принимает на вход один аргумент:
    year — натуральное число, год

Функция должна возвращать количество воскресений в году year.

Sample Input 1:
print(num_of_sundays(2021))

Sample Output 1:
52

Sample Input 2:

year = 2000
print(num_of_sundays(year))

Sample Output 2:
53

Sample Input 3:
print(num_of_sundays(768))

Sample Output 3:
52

"""

from datetime import timedelta, date


# def is_leap_year(y: int) -> bool:
#     """Принимает y - год и проверяет, является ли он вискокосным """
#     if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
#         return False
#     return True


# def num_of_sundays(year: int):
#     """ Принимает на вход один аргумент: year — натуральное число, год
#     и возвращает количество воскресений в году year"""
#     d1 = date(year, 1, 1)
#     d2 = d1 + timedelta(days=(365, 366)[is_leap_year(year)])
#     return sum(date.fromordinal(d).weekday() == 6 for d in range(d1.toordinal(), d2.toordinal()))


# def num_of_sundays(year):
#     counter, td = 0, timedelta(days=7)
#     d = date(year, 1, 1)
#     d += timedelta(days=6 - d.weekday())
#     while d.year == year:
#         d += td
#         counter += 1
#     return counter


def num_of_sundays(y):
    return date(y, 12, 31).strftime("%U")  # Номер недели в году


print(num_of_sundays(2000))
# 53
print(num_of_sundays(768))
# 52
print(num_of_sundays(1944))
# 53
print(num_of_sundays(2022))
# 52
print(num_of_sundays(2050))
# 52
