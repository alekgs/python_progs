"""
Средняя зарплата
Вам доступен файл salary_data.csv, который содержит анонимную информацию о зарплатах сотрудников
в различных компаниях. В первом столбце записано название компании, а во втором — зарплата очередного сотрудника:

company_name;salary
Atos;135000
ХайТэк;24400
Philax;128600
Инлайн Груп;43900
IBS;70600
Oracle;131600
Atos;91000
...

Напишите программу, которая упорядочивает компании по возрастанию средней зарплаты ее сотрудников и выводит их
названия, каждое на отдельной строке. Если две компании имеют одинаковые средние зарплаты, они должны быть
расположены в лексикографическом порядке их названий.

Примечание 1. Средняя зарплата компании определяется как отношение суммы всех зарплат к их количеству.
Примечание 2. Разделителем в файле salary_data.csv является точка с запятой, при этом кавычки не используются.
Примечание 3. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 4. Начальная часть ответа выглядит так:

Информзащита
Форс
OFT group
...

Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.
"""

# через Pandas
# import pandas as pd
# import time
# t_start = time.perf_counter()
# df_salary = pd.read_csv('salary_data.csv', sep=';')
# print(*df_salary.groupby('company_name').mean().sort_values(['salary', 'company_name']).index, sep='\n')
# t_end = time.perf_counter()
# print(t_end - t_start)


# через словарь
import csv
# import time
# t_start = time.perf_counter()
d = {}
with open('salary_data.csv', encoding='utf-8') as file:
    rows = list(csv.reader(file, delimiter=';'))
    for key, value in rows[1:]:
        d[key] = d.get(key, []) + [int(value)]

d_sort = sorted(d, key=lambda x: (sum(d[x]) / len(d[x]), x))
print(*d_sort, sep='\n')
# t_end = time.perf_counter()
# print(t_end - t_start)
