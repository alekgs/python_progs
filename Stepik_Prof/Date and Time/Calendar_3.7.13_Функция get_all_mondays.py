"""
Функция get_all_mondays()
Реализуйте функцию get_all_mondays(), которая принимает один аргумент year — натуральное число
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) года year,
выпадающих на понедельник.

Примечание 1.
Например, вызов get_all_mondays(2021)

должен вернуть список:
[datetime.date(2021, 1, 4), datetime.date(2021, 1, 11), ..., datetime.date(2021, 12, 20), datetime.date(2021, 12, 27)]
"""

from datetime import date
from calendar import monthcalendar


def get_all_mondays(y: int) -> list:
    """Возвращает список дат понедельников года в формате datetime"""
    return [date(y, m, d[0]) for m in range(1, 13) for d in monthcalendar(y, m) if d[0]]

# def get_all_mondays(y: int) -> list:
#     """Возвращает список дат понедельников года в формате datetime"""
#     mondays = []
#     [[mondays.append(date(y, m, d[0])) for d in monthcalendar(y, m) if d[0]] for m in range(1, 13)]
#
#     return mondays
#


print(get_all_mondays(2023))
