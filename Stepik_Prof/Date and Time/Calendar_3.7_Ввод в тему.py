import calendar
import locale

# win
locale.setlocale(locale.LC_ALL, 'ru-RU')

# unix/linux
#locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

# print day names
[print(name.title(), end=' ') for name in calendar.day_name]
# 'Понедельник Вторник Среда Четверг Пятница Суббота Воскресенье'
print()
[print(name, end=' ') for name in calendar.day_name]
# понедельник вторник среда четверг пятница суббота воскресенье
print()
# list
names = list(calendar.day_name)
print(names)

# day abbreviates - сокращенное название дня
[print(name, end=' ') for name in calendar.day_abbr]
# 'Пн Вт Ср Чт Пт Сб Вс'
print()

# months
# атрибут month_name соответствует обычному соглашению, что январь – это месяц номер 1,
# поэтому список имеет длину в 13 элементов, первый из которых – пустая строка.
months = list(calendar.month_name)
print(months)
# ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь',
# 'Декабрь']

# months abbreviates - сокращенное название месяца
months_abbr = list(calendar.month_abbr)
print(*map(lambda m: m.title(), months_abbr), end=' ')
# ' Янв Фев Мар Апр Май Июн Июл Авг Сен Окт Ноя Дек'

# Для получения номеров дней недели можно использовать атрибуты: MONDAY, TUESDAY, ..., SUNDAY.
print(calendar.MONDAY)     # 1
print(calendar.TUESDAY)    # 2
print(calendar.WEDNESDAY)  # 3
print(calendar.THURSDAY)   # 4
print(calendar.FRIDAY)     # 5
print(calendar.SATURDAY)   # 6
print(calendar.SUNDAY)     # 7

# Проверка на високосный год
print(calendar.isleap(2020))
print(calendar.isleap(2024))

# Функция leapdays(y1, y2) возвращает количество високосных лет в диапазоне от y1 до y2 (исключая), где y1 и y2 – годы.
# Приведенный ниже код:
print(calendar.leapdays(2020, 2025))  # 2, т.к. в диапазоне 2020 -2025 находятся два високосных года: 2020 и 2024.

# Функция monthrange(year, month) возвращает день недели первого дня месяца и количество дней
# в месяце в виде кортежа для указанного года year и месяца month.
print(calendar.monthrange(2022, 1))     # (5, 31) 5 день  - суббота январь 2022 года, 31 день в месяце
print(calendar.monthrange(2021, 9))     # (2, 30) 1 день - среда сентябрь 2021 года, 30 дней в месяце

# Функция monthcalendar(year, month) возвращает матрицу, представляющую календарь на месяц.
# Каждая строка матрицы представляет неделю.
# Обратите внимание на то, что дни, которые не входят в указанный месяц, представлены нулями.
# При этом каждая неделя начинается с понедельника, если не установлено другое функцией setfirstweekday()

print(*calendar.monthcalendar(2021, 9), sep='\n')
print()
# [0, 0, 1, 2, 3, 4, 5]
# [6, 7, 8, 9, 10, 11, 12]
# [13, 14, 15, 16, 17, 18, 19]
# [20, 21, 22, 23, 24, 25, 26]
# [27, 28, 29, 30, 0, 0, 0]

# Функция month(year, month, w=0, l=0) возвращает календарь на месяц в многострочной строке.
# Аргументами функции являются: year (год), month (месяц), w (ширина столбца даты)
# и l (количество строк, отводимые на неделю).
# Аргументы w и l имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.

print(calendar.month(2023, 1))
print(calendar.month(2021, 10))
print(calendar.month(2021, 9, w=3))
print(calendar.month(2021, 9, l=2))
print(calendar.month(2021, 9, w=5, l=2))

#    September 2021
# Mo Tu We Th Fr Sa Su
#        1  2  3  4  5
#  6  7  8  9 10 11 12
# 13 14 15 16 17 18 19
# 20 21 22 23 24 25 26
# 27 28 29 30
#
#     October 2021
# Mo Tu We Th Fr Sa Su
#              1  2  3
#  4  5  6  7  8  9 10
# 11 12 13 14 15 16 17
# 18 19 20 21 22 23 24
# 25 26 27 28 29 30 31
#
#        September 2021
# Mon Tue Wed Thu Fri Sat Sun
#           1   2   3   4   5
#   6   7   8   9  10  11  12
#  13  14  15  16  17  18  19
#  20  21  22  23  24  25  26
#  27  28  29  30
#
#    September 2021
#
# Mo Tu We Th Fr Sa Su
#
#        1  2  3  4  5
#
#  6  7  8  9 10 11 12
#
# 13 14 15 16 17 18 19
#
# 20 21 22 23 24 25 26
#
# 27 28 29 30
#
#
#               September 2021
#
#  Mon   Tue   Wed   Thu   Fri   Sat   Sun
#
#                1     2     3     4     5
#
#    6     7     8     9    10    11    12
#
#   13    14    15    16    17    18    19
#
#   20    21    22    23    24    25    26
#
#   27    28    29    30
#

# Функция calendar(year, w=2, l=1, c=6, m=3) возвращает календарь на весь год в виде многострочной строки.
# Аргументами функции являются: year (год),  w (ширина столбца даты) и l (количество строк, отводимые на неделю),
# c (количество пробелов между столбцом месяца),  m (количество столбцов).
# Аргументы w, l, c, m имеют значения по умолчанию, поэтому их можно не передавать явно при вызове функции.

print(calendar.calendar(2023))
#
#                                   2021
#
#       January                   February                   March
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#              1  2  3       1  2  3  4  5  6  7       1  2  3  4  5  6  7
#  4  5  6  7  8  9 10       8  9 10 11 12 13 14       8  9 10 11 12 13 14
# 11 12 13 14 15 16 17      15 16 17 18 19 20 21      15 16 17 18 19 20 21
# 18 19 20 21 22 23 24      22 23 24 25 26 27 28      22 23 24 25 26 27 28
# 25 26 27 28 29 30 31                                29 30 31
#
#        April                      May                       June
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                      1  2          1  2  3  4  5  6
#  5  6  7  8  9 10 11       3  4  5  6  7  8  9       7  8  9 10 11 12 13
# 12 13 14 15 16 17 18      10 11 12 13 14 15 16      14 15 16 17 18 19 20
# 19 20 21 22 23 24 25      17 18 19 20 21 22 23      21 22 23 24 25 26 27
# 26 27 28 29 30            24 25 26 27 28 29 30      28 29 30
#                           31
#
#         July                     August                  September
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#           1  2  3  4                         1             1  2  3  4  5
#  5  6  7  8  9 10 11       2  3  4  5  6  7  8       6  7  8  9 10 11 12
# 12 13 14 15 16 17 18       9 10 11 12 13 14 15      13 14 15 16 17 18 19
# 19 20 21 22 23 24 25      16 17 18 19 20 21 22      20 21 22 23 24 25 26
# 26 27 28 29 30 31         23 24 25 26 27 28 29      27 28 29 30
#                           30 31
#
#       October                   November                  December
# Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su      Mo Tu We Th Fr Sa Su
#              1  2  3       1  2  3  4  5  6  7             1  2  3  4  5
#  4  5  6  7  8  9 10       8  9 10 11 12 13 14       6  7  8  9 10 11 12
# 11 12 13 14 15 16 17      15 16 17 18 19 20 21      13 14 15 16 17 18 19
# 18 19 20 21 22 23 24      22 23 24 25 26 27 28      20 21 22 23 24 25 26
# 25 26 27 28 29 30 31      29 30                     27 28 29 30 31

