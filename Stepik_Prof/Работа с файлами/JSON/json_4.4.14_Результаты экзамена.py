"""
Результаты экзамена 🌶️

Вам доступен файл exam_results.csv, который содержит информацию о прошедшем экзамене в некотором учебном заведении. В
первом столбце записано имя студента, во втором — фамилия, в третьем — оценка за экзамен, в четвертом — дата и время
сдачи в формате YYYY-MM-DD HH:MM:SS, в пятом — адрес электронной почты:

name,surname,score,date_and_time,email
Jayson,Edwards,2,2021-11-10 10:00:00,sonnen@yahoo.com
April,Sims,3,2021-11-01 11:00:00,retoh@outlook.com
...

Каждый студент имеет право пересдать экзамен два раза, поэтому он может встречаться в исходном файле до трёх раз с
различной оценкой и различными датой и временем сдачи.

Напишите программу, которая для каждого студента определяет его максимальную оценку, а также дату и время ее
получения. Программа должна создать список словарей, каждый из которых содержит следующие пары ключ-значение:


    name — имя студента
    surname — фамилия студента
    best_score — максимальная оценка за экзамен
    date_and_time — дата и время получения максимальной оценки в исходном формате
    email — адрес электронной почты

Полученный список программа должна записать в файл best_scores.json, причем словари в списке должны быть расположены
в лексикографическом порядке названий электронных почт.

Примечание 1. Если при пересдаче студент получил такую же оценку, что и в прошлый раз, то в качестве даты следует
указать дату пересдачи.
Примечание 2. В качестве разделителя в файле exam_results.csv используется запятая, при этом кавычки не используются.
Примечание 3. Начальная часть файла best_scores.json выглядит так:

[
   {
      "name": "Stephen",
      "surname": "Farley",
      "best_score": 3,
      "date_and_time": "2021-11-12 12:00:00",
      "email": "aardo@mac.com"
   },
   {
      "name": "Kaylen",
      "surname": "Horne",
      "best_score": 4,
      "date_and_time": "2021-11-09 11:00:00",
      "email": "aaribaud@att.net"
   },
   ...
]

Решение
Идея заключается в следующем:
1) Считываем файл, тут всё понятно.
2) При итерации в одной строке сразу удаляем ключ 'score' и записываем его значение под ключом 'best_score'
3) Из результирующего словаря получаем значение по ключу 'email'.
   Если его ещё там нет, то значением будет словарь, полученный из файла на текущей итерации

4) Из двух словарей (первый — очередной словарь из файла, второй — словарь, полученный на шаге 33) выбираем тот,
в котором оценка выше. Если оценки совпадают, будет выбран тот, у которого более поздняя дата.

5) В результирующий словарь по ключу 'email', взятом из словаря, находящегося в файле, записываем значение из шага 4
6) Сортируем значения результирующего словаря по ключу 'email'
7) Записываем результат в новый файл

Тем самым, за одну итерацию по входящему файлу отобрали наилучшие оценки каждого из учеников, затем отсортировали и
сохранили в результирующий файл

"""
# import csv
# import json

import pandas as pd

df = pd.read_csv('exam_results.csv')
df_out = df.groupby(['name', 'surname'], as_index=False).agg(max)
df_out = df_out.sort_values('email').rename(columns={'score': 'best_score'})
df_out.to_json('best_scores.json', orient='records', indent=3)



# Решение № 1
# from datetime import datetime as dt
#
# result = {}
# with open('exam_results.csv', encoding='utf-8') as ex_r:
#     for row in csv.DictReader(ex_r): # 1
#         row['best_score'] = int(row.pop('score'))  # 2
#         r = result.get(row['email'], row)  # 3
#         best_row = max(r, row, key=lambda item: (item['best_score'], item['date_and_time']))  # 4
#         result[row['email']] = best_row  # 5
#
# with open('best_scores.json', 'w', encoding='utf-8') as bs:
#     out = sorted(result.values(), key=lambda item: item['email'])  # 6
#     json.dump(out, bs, indent=3)  # 7
#

# Мое решение

# with (open('exam_results.csv', encoding='utf-8') as f_in,
#       open('best_scores.json', 'w', encoding='utf-8') as f_out):
#     res, res_out = {}, []
#     mask_dt = '%Y-%m-%d %H:%M:%S'
#     for s in csv.DictReader(f_in):
#         d_ex = dt.strptime(s['date_and_time'], mask_dt)
#         res.setdefault((s['email'], s['name'], s['surname']), {}).setdefault(int(s['score']), []).append(d_ex)
#
#     for k, v in res.items():
#         max_sc = max(v.keys())
#         date = dt.strftime(max(v[max_sc]), mask_dt)
#         d_out = {'name': k[1], 'surname': k[2], 'best_score': max_sc, 'date_and_time': date, 'email': k[0]}
#         res_out.append(d_out)
#
#     json.dump(sorted(res_out, key=lambda x: x['email']), f_out, indent=3)

# ##### Решение 3
# with open('exam_results.csv', encoding='utf8') as f_in:
#     header, *rows = csv.reader(f_in)
#
# # сортируем полученный список по email, score, date_and_time
# rows.sort(key=lambda x: (x[4], x[2], x[3]))
#
# # формируем словарь
# res = {}
# for name, surname, score, date, email in rows:
#     res[email] = {
#                  'name': name,
#                  'surname': surname,
#                  'best_score': int(score),
#                  'date_and_time': date,
#                  'email': email
#                  }
#
# # выгружаем в json
# with open('best_scores.json', 'w', encoding='utf8') as f_out:
#     json.dump(list(res.values()), f_out, indent=3)
