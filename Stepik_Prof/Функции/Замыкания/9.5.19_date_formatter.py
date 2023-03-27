"""
Функция date_formatter()

Нередко в разных странах используются разные форматы дат.
Рассмотрим часть из них:
код страны 	формат даты
ru 	DD.MM.YYYY
us 	MM-DD-YYYY
ca 	YYYY-MM-DD
br 	DD/MM/YYYY
fr 	DD.MM.YYYY
pt 	DD-MM-YYYY

Реализуйте функцию date_formatter(), которая принимает один аргумент:
    country_code — код страны

Функция date_formatter() должна возвращать функцию, которая принимает в качестве аргумента дату
(тип date) и возвращает строку с данной датой в формате страны с кодом country_code.


Sample Input 1:

date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

Sample Output 1:
25.01.2022

Sample Input 2:
date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))

Sample Output 2:
01-05-2025

Sample Input 3:
date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))

Sample Output 3:
2015-12-07


ru 	DD.MM.YYYY
us 	MM-DD-YYYY
ca 	YYYY-MM-DD
br 	DD/MM/YYYY
fr 	DD.MM.YYYY
pt 	DD-MM-YYYY

"""
from datetime import date


def date_formatter(country_code):
    date_formats = {'ru': '%d.%m.%Y', 'us': '%m-%d-%Y',
                    'ca': '%Y-%m-%d', 'br': '%d/%m/%Y',
                    'fr': '%d.%m.%Y', 'pt': '%d-%m-%Y'}
    return lambda dt: dt.strftime(date_formats[country_code])

# def date_formatter(country_code):
#     def get_date(d):
#         match country_code:
#             case 'ru' | 'fr':
#                 date_format = '%d.%m.%Y'
#             case 'us':
#                 date_format = '%m-%d-%Y'
#             case 'ca':
#                 date_format = '%Y-%m-%d'
#             case 'br':
#                 date_format = '%d/%m/%Y'
#             case 'pt':
#                 date_format = '%d-%m-%Y'
#         return date.strftime(d, date_format)
#     return get_date


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))

date_ru = date_formatter('us')
today = date(2025, 1, 5)
print(date_ru(today))

date_ru = date_formatter('ca')
today = date(2015, 12, 7)
print(date_ru(today))
