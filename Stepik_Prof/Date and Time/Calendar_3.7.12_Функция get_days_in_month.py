"""
Функция get_days_in_month()

Реализуйте функцию get_days_in_month(), которая принимает два аргумента в следующем порядке:
    year — натуральное число
    month — полное название месяца на английском
Функция должна возвращать отсортированный по возрастанию список всех дат (тип date) месяца month
и года year.
Примечание 1. Например, вызов:
get_days_in_month(2021, 'December')

должен вернуть список:
[datetime.date(2021, 12, 1), datetime.date(2021, 12, 2), ..., datetime.date(2021, 12, 30),
datetime.date(2021, 12, 31)]


"""
from datetime import date
from calendar import month_name, monthrange


def get_days_in_month(y: int, m: str) -> list:
    """Возвращает список дат месяца в формате datetime"""
    m = list(month_name).index(m)
    d_count = monthrange(int(y), m)[1]

    return [date(y, m, d) for d in range(1, d_count + 1)]


print(get_days_in_month(2021, 'December'))
