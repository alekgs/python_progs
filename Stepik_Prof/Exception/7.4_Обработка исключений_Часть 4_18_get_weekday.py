"""
Функция get_weekday()

Реализуйте функцию get_weekday(), которая принимает один аргумент:

    number — целое число (от 1 до 7 включительно)

Функция должна возвращать полное название дня недели на русском, который соответствует числу number, при этом:
    если number не является целым числом, функция должна возбуждать исключение:
    TypeError('Аргумент не является целым числом')
    если number является целым числом, но не принадлежит отрезку [1;7], функция должна возбуждать исключение:
    ValueError('Аргумент не принадлежит требуемому диапазону')



"""
from calendar import day_name
import locale

# for k, v in locale.locale_alias.items():
#     print(f'{k}: {v}')

locale.setlocale(locale.LC_ALL, 'ru-RU')
# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')


def get_weekday(number):
    days = {n: m.title() for n, m in enumerate(day_name, 1)}
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if number not in days.keys():
        raise ValueError('Аргумент не принадлежит требуемому диапазону')
    else:
        return days[number]


# Sample Input 1:
print(get_weekday(1))

# Sample Output 1:
# Понедельник

# Sample Input 2:
try:
    print(get_weekday('hello'))
except Exception as err:
    print(err)
    print(type(err))

# Sample Output 2:
# Аргумент не является целым числом
# <class 'TypeError'>

# Sample Input 3:
try:
    print(get_weekday(0))
except ValueError as err:
    print(err)
    print(type(err))

# Sample Output 3:
# Аргумент не принадлежит требуемому диапазону
# <class 'ValueError'>
