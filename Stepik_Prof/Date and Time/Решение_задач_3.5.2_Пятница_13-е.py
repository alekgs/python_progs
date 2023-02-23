"""
Число 13 считалось дьявольским издавна. Это имеет свое объяснение, и не одно: тут есть трактовки, связанные с
Тайной вечерей — где были Христос и 12 апостолов, один из которых стал предателем. Есть поверье, что для шабаша
нужны 12 ведьм и сатана. В истории число 13 в связке с пятницей стало «несчастливым» в 1307 году,
когда король Франции Филипп Красивый отдал приказ схватить всех тамплиеров — членов рыцарского ордена крестоносцев.
Все они были сожжены на кострах инквизиции, и произошло это в пятницу, 13 апреля.

Докажите, что 13-е число месяца чаще всего приходится на пятницу.
Напишите программу, которая вычисляет, сколько тринадцатых чисел приходится на каждый день недели
в период с 01.01.0001 по 31.12.9999.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных Программа должна вывести 7 чисел — количество тринадцатых чисел, которые приходятся на
понедельник, вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999.
Числа должны быть расположены каждое на отдельной строке.
"""

from datetime import date, datetime, timedelta
import time


# Мой вариант  - перебором цикл for
t1 = time.perf_counter()

start = datetime(year=1, month=1, day=1)
end = datetime(year=9999, month=12, day=31)

day13_count = {}

for d in range(start.toordinal(), end.toordinal() + 1):
    if datetime.fromordinal(d).day == 13:
        d_week = datetime.fromordinal(d).weekday()
        day13_count[d_week] = day13_count.get(d_week, 0) + 1

[print(v) for k, v in sorted(day13_count.items())]
t2 = time.perf_counter()
print(t2 - t1)

# Вариант 2 - список
t1 = time.perf_counter()
count = [0] * 7
for years in range(1, 10000):
    for months in range(1, 13):
        count[date(years, months, 13).weekday()] += 1
print(*count, sep='\n')
t2 = time.perf_counter()
print(t2 - t1)

# Вариант 4 - словарь
# t1 = time.perf_counter()
# week = {}
# for y in range(1, 10000):
#     for m in range(1, 13):
#         key = date(y, m, 13).weekday()
#         week[key] = week.get(key, 0) + 1
#
# # for i in range(7):
# #     print(week[i])
# [print(f'Day of week {k}: {v}') for k, v in sorted(week.items())]
# print(time.perf_counter() - t1)


# Вариант 4 - collections Counter
# from collections import Counter
# t1 = time.perf_counter()
# weekdays = Counter([date(year=i, month=j, day=13).isoweekday() for i in range(1, 10000) for j in range(1, 13)])
# [print(weekdays[i]) for i in range(1, 8)]
# t2 = time.perf_counter()
# print(t2 - t1)

