"""
Лог-файл

Вам доступен файл name_log.csv, в котором находятся логи изменения имени пользователя. В первом столбце записано
измененное имя пользователя, во втором — адрес электронной почты, в третьем — дата и время изменения. При этом email
пользователь менять не может, только имя:

username,email,dtime
rare_charles6,charlesthompson@inbox.ru,15/11/2021 08:15
busy_patricia5,patriciasmith@bk.ru,07/11/2021 08:07
...

Напишите программу, которая отбирает из файла name_log.csv только самые свежие записи для каждого пользователя и
записывает их в файл new_name_log.csv. В файле new_name_log.csv первой строкой должны быть заголовки столбцов такие
же, как в файле name_log.csv. Логи в итоговом файле должны быть расположены в лексикографическом порядке названий
электронных ящиков пользователей.

Примечание 1. Для части пользователей в исходном файле запись только одна, и тогда в итоговый файл следует записать
только ее, для некоторых пользователей есть несколько записей с разными именами.

Например, пользователь с электронной почтой c3po@gmail.com несколько раз менял имя:

C=3PO,c3po@gmail.com,16/11/2021 17:10
C3PO,c3po@gmail.com,16/11/2021 17:15
C-3PO,c3po@gmail.com,16/11/2021 17:24

Из этих трех записей в итоговый файл должна быть записана только одна — самая свежая:
C-3PO,c3po@gmail.com,16/11/2021 17:24

Примечание 2. Разделителем в файле name_log.csv является запятая, при этом кавычки не используются.

Примечание 3. Начальная часть файла new_name_log.csv выглядит так:
username,email,dtime
angry-barbara2,barbaraanderson@bk.ru,17/11/2021 01:17
dead-barbara6,barbarabrown@rambler.ru,27/11/2021 08:27
busy_barbara7,barbaradavis@aol.com,24/11/2021 08:24
...

"""
import csv
from datetime import datetime as dt

with open('name_log.csv', encoding='UTF-8') as f:
    header, *rows = csv.reader(f)
    d = {i[1]: i for i in sorted(rows, key=lambda x: dt.strptime(x[2], '%d/%m/%Y %H:%M'))}

with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f_out:
    w = csv.writer(f_out)
    w.writerow(header)
    w.writerows(sorted(d.values(), key=lambda x: x[1]))

# with open('name_log.csv', encoding='utf-8') as f:
#     rows, result = csv.DictReader(f, delimiter=','), {}
#     for row in rows:
#         date_log = dt.strptime(row['dtime'], '%d/%m/%Y %H:%M')
#         result[row['email']] = result.get(row['email'], {}) | {date_log: row['username']}
#
# with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as f_out:
#     f_out.write('username,email,dtime\n')
#     for k, v in sorted(result.items()):
#         last_update = max(v)
#         f_out.write(f"{v[last_update]},{k},{last_update.strftime('%d/%m/%Y %H:%M')}\n")


