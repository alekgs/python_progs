"""
Во время визита очередного гостя сотрудникам отеля приходится проверять, доступна ли та или иная дата для
бронирования номера.

Реализуйте функцию is_available_date(), которая принимает два аргумента в следующем порядке:
    booked_dates — список строковых дат, недоступных для бронирования.
    Элементом списка является либо одиночная дата, либо период (две даты через дефис).

    Например:
    ['04.11.2021', '05.11.2021-09.11.2021']

    date_for_booking — одиночная строковая дата или период (две даты через дефис), на которую гость желает
    забронировать номер.
    Например:
    '01.11.2021' или '01.11.2021-04.11.2021'

Функция is_available_date() должна возвращать True, если дата или период date_for_booking полностью доступна для
бронирования. В противном случае функция должна возвращать False.

Примечание 1. Гарантируется, что в периоде левая дата всегда меньше правой.
Примечание 2. В периоде (две даты через дефис) граничные даты включены.

"""
from datetime import datetime, timedelta


def str_to_date(st_date: list | str) -> list:
    """Создает дату из строки и возвращает список в формате datetime"""
    if isinstance(st_date, str):
        st_date = [st_date]

    def s2d(s: str) -> datetime:
        return datetime.strptime(s, '%d.%m.%Y')

    b_dts = []
    for dt in st_date:
        if len(dt) == 10:
            b_dts.append(s2d(dt))
        else:
            d1, d2 = map(s2d, dt.split('-'))
            [b_dts.append(d1 + timedelta(i)) for i in range((d2 - d1).days + 1)]
    return b_dts


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    """Возвращает True, если дата или период date_for_booking полностью доступна
       для бронирования, иначе возвращает False"""

    bd_list = str_to_date(booked_dates)
    d_list = str_to_date(date_for_booking)

    if len(d_list) == 1:
        return (True, False)[d_list[0] in bd_list]
    else:
        return (False, True)[max(d_list) < min(bd_list) or min(d_list) > max(bd_list)]


# Тесты
# 1
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021'
print(is_available_date(dates, some_date))
# True
#
# 2
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
# False

# 3
dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))
# False

# 4
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '12.11.2021'
print(is_available_date(dates, some_date))
# False

# 5
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021'
print(is_available_date(dates, some_date))
# False

# 6
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '15.11.2021'
print(is_available_date(dates, some_date))
# False

# 7
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '17.11.2021'
print(is_available_date(dates, some_date))
# False

# 8
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '22.11.2021-25.11.2021'
print(is_available_date(dates, some_date))
# True

# 9
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '01.11.2021-04.11.2021'
print(is_available_date(dates, some_date))
# False

# 10
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '02.11.2021-05.11.2021'
print(is_available_date(dates, some_date))
# False

# 11
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '10.11.2021-14.11.2021'
print(is_available_date(dates, some_date))
# False

# 12
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '03.11.2021-05.11.2021'
print(is_available_date(dates, some_date))
# False

# 13
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '09.11.2021-10.11.2021'
print(is_available_date(dates, some_date))
# False

# 14
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '06.11.2021-08.11.2021'
print(is_available_date(dates, some_date))
# False

# 15
dates = ['01.11.2021', '05.11.2021-09.11.2021', '12.11.2021', '15.11.2021-21.11.2021']
some_date = '14.11.2021-22.11.2021'
print(is_available_date(dates, some_date))
# False

# 16
dates = ['14.09.2022-14.10.2022']
some_date = '20.09.2022'
print(is_available_date(dates, some_date))
# False

# 17
dates = ['14.09.2022-14.10.2022']
some_date = '14.11.2022'
print(is_available_date(dates, some_date))
# True

# 18
dates = ['14.09.2022-14.10.2022']
some_date = '15.11.2022-16.11.2022'
print(is_available_date(dates, some_date))
# True

# 19
dates = ['14.09.2022-14.10.2022']
some_date = '14.09.2022-22.09.2022'
print(is_available_date(dates, some_date))
# False


# 20
dates = ['02.11.2021', '05.11.2021-09.11.2021']
some_date = '03.11.2021'
print(is_available_date(dates, some_date))
# True
