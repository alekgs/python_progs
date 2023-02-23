"""
Вам доступны список dates, содержащий даты, и список times, содержащий времена. Количество элементов в этих
списках одинаковое. Дополните приведенный ниже код, чтобы он вывел datetime объекты, полученные путем объединения
элементов списков dates и times, находящихся на одинаковых позициях. Полученные объекты должны быть расположены в
порядке возрастания секунд, каждый на отдельной строке.

Примечание 1. Например, если бы списки dates и times имели вид:

dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]

то программа должна была бы вывести:
2021-07-02 12:19:01
2020-09-25 07:30:01
2020-11-12 12:50:22

Примечание 2. Если объекты имеют равное количество секунд, то следует сохранить их исходный порядок.

"""
from datetime import datetime, date, time
from operator import attrgetter

dates = [date(1793, 8, 23), date(1410, 3, 11), date(804, 11, 12), date(632, 6, 4),
         date(295, 1, 23), date(327, 8, 24), date(167, 4, 16), date(229, 1, 24),
         date(1239, 2, 5), date(1957, 7, 14), date(197, 8, 24), date(479, 9, 6)]

times = [time(7, 33, 27), time(21, 2, 10), time(17, 20, 47), time(20, 8, 59),
         time(12, 42, 56), time(15, 9, 57), time(17, 47, 9), time(9, 40, 2),
         time(11, 47, 1), time(17, 27, 10), time(17, 55, 40), time(9, 14, 9)]

# 1
# print(*sorted([datetime.combine(d, t) for d, t in zip(dates, times)], key=lambda t: t.second), sep='\n')

# 2
# dt = [datetime.combine(d, t) for d, t in zip(dates, times)]
# print(*sorted(dt, key=attrgetter('second')), sep='\n')

# 3
dt = map(datetime.combine, dates, times)
print(*sorted(dt, key=lambda x: x.second), sep='\n')
