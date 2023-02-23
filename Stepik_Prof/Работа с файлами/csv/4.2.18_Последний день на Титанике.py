"""
Последний день на Титанике

Вам доступен файл titanic.csv, который содержит данные о пассажирах, присутствовавших на борту парохода Титаник.
В первом столбце указана единица, если пассажир выжил, и ноль в противном случае, во втором столбце записано полное имя
пассажира, в третьем — пол, в четвертом — возраст:

survived;name;sex;age
0;Mr. Owen Harris Braund;male;22
1;Mrs. John Bradley (Florence Briggs Thayer) Cumings;female;38
...

Напишите программу, которая выводит имена выживших пассажиров, которым было менее 1818 лет, каждое на отдельной
строке. Причем сначала должны быть расположены имена всех пассажиров мужского пола, а затем — женского,
имена же непосредственно в мужском и женском списках должны быть расположены в своем исходном порядке.

Примечание 1. Разделителем в файле titanic.csv является точка с запятой, при этом кавычки не используются.
Примечание 3. Часть ответа выглядит так:

Master. Gerios Moubarek
Master. Alden Gates Caldwell
...
Master. Harold Theodor Johnson
Mrs. Nicholas (Adele Achem) Nasser
Miss. Marguerite Rut Sandstrom
...

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.
"""
# from time import perf_counter
# import pandas as pd
# start = perf_counter()
# df = pd.read_csv('titanic.csv', sep=';')
# mask = (df.survived == 1) & (df.age < 18)
# print(*df[mask][['name', 'sex']].sort_values(['sex'], ascending=False, kind='stable')['name'], sep='\n')
# print()
# print(perf_counter() - start)
#
import csv

with open('titanic.csv', encoding='utf-8') as f:
    rows, result = csv.DictReader(f, delimiter=';'), {}
    for row in rows:
        if int(row['survived']) == 1 and float(row['age']) < 18:
            result[row['name']] = row['sex']

print(*sorted(result, key=lambda k: result[k], reverse=True), sep='\n')
