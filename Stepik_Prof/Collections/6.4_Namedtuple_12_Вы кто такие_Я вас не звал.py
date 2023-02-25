"""
Вы кто такие? Я вас не звал

У Тимура имеется немало друзей из других городов или стран, которые часто приезжают к нему в гости с целью увидеться
и развлечься. Чтобы не забыть ни об одной встрече, Тимур записывает имена и фамилии друзей в csv файл, дополнительно
указывая для каждого дату и время встречи. Вам доступен этот файл, имеющий название meetings.csv, в котором в первом
столбце записана фамилия, во втором — имя, в третьем — дата в формате DD.MM.YYYY , в четвертом — время в формате HH:MM:

surname,name,meeting_date,meeting_time
Харисов,Артур,15.07.2022,17:00
Геор,Гагиев,14.12.2022,18:00
...

Напишите программу, которая выводит фамилии и имена друзей Тимура, предварительно отсортировав их по дате и времени
встречи от самой ранней до самой поздней. Фамилии и имена должны быть расположены каждые на отдельной строке.

Примечание 1. Начальная часть ответа выглядит так:

Гудцев Таймураз
Харисов Артур
Базиев Герман
...

Примечание 2. Гарантируется, что никакие две встречи не имеют одновременно одинаковые даты и время.
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 4. Разделителем в файле meetings.csv является запятая, при этом кавычки не используются.
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""

from collections import namedtuple
import csv
from datetime import datetime as dt

Meeting = namedtuple('Meeting', ['surname', 'name', 'date', 'time'])

with open('meetings.csv', encoding='utf-8') as file:
    next(rows := csv.reader(file))
    data = [Meeting._make(row) for row in rows]

res = sorted(data, key=lambda x: dt.strptime(x.date + x.time, '%d.%m.%Y%H:%M'))
[print(i.surname, i.name) for i in res]


# Через Pandas )

# import pandas as pd
# df = pd.read_csv('meetings.csv')
#
# df['meeting_dt'] = df.meeting_date + df.meeting_time
# df.meeting_dt = pd.to_datetime(df.meeting_dt, format='%d.%m.%Y%H:%M')
#
# df.sort_values('meeting_dt', inplace=True)
# df['full_name'] = df.surname + ' ' + df.name
#
# print(*df.full_name, sep='\n')

