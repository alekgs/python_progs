from datetime import datetime


def set_of_date(st_date: list | str) -> set:
    """Создает дату из строки и возвращает множество в формате datetime.toordinal()"""
    if isinstance(st_date, str):
        st_date = [st_date]

    def s2d(s: str) -> int:
        """Переводит строку в формат datetime.toordinal()"""
        return datetime.strptime(s, '%d.%m.%Y').toordinal()

    d_set = set()
    for dt in st_date:
        if len(dt) == 10:
            d_set.add(s2d(dt))
        else:
            d1, d2 = map(s2d, dt.split('-'))
            [d_set.add(d1 + i) for i in range((d2 - d1) + 1)]
    return d_set


def is_available_date(booked_dates: list, date_for_booking: str) -> bool:
    """Возвращает True, если дата или период date_for_booking полностью доступна
       для бронирования, иначе возвращает False"""
    bd_list = set_of_date(booked_dates)
    d_list = set_of_date(date_for_booking)

    return len(d_list & bd_list) == 0


# Тесты
# 1
dates = ['04.11.2021', '02.11.2021', '05.11.2021-09.11.2021']
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
some_date = '15.11.2022'
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
