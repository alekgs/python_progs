def is_leap_year(year: int) -> bool | None:
    """Определяет, является ли год високосным. Год будет високосным, если он делится без остатка на 400,
       или он одновременно делится без остатка на 4 и не делится на 100"""
    return year % 400 == 0 or (year % 100 != 0 and year % 4 == 0)


year_in = int(input())
print((f'{year_in} г. - невисокосный', f'{year_in} г. - високосный')[is_leap_year(year_in)])
