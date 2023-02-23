"""
Проще, чем кажется 🌶️

Рассмотрим следующий текстовый фрагмент:
ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none

Каждая строка этого фрагмента содержит три значения через запятую: имя объекта, свойство этого объекта,
значение свойства. Например, в первой строке указан объект ball, имеющий свойство color, значение которого равно
purple. Также у объекта ball есть свойства size и notes, имеющие значения 4 и it's round соответственно. Помимо
объекта ball имеется объект cup, имеющий те же свойства и в том же количестве. Дадим этим объектам общее название
object и сгруппируем строки данного текстового фрагмента по первому столбцу:

object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none

Мы получили запись в привычном CSV формате, в котором в первом столбце указывается имя объекта, а в последующих —
значения соответствующих свойств этого объекта.

Реализуйте функцию condense_csv(), которая принимает два аргумента в следующем формате:

    filename — название csv файла, например, data.csv; формат содержимого файла аналогичен формату текстового
    фрагмента, рассмотренного в условии задачи: каждая строка файла содержит три значения через запятую, а именно имя
    объекта, свойство этого объекта, значение свойства; все объекты имеют равные свойства и в равных количествах
    id_name — общее название для объектов

Функция должна привести содержимое файла в привычный CSV формат, сгруппировав строки по первому столбцу и назвав
первый столбец id_name. Полученный результат функция должна записать в файл condensed.csv.

Примечание 1. Например, если бы файл data.csv имел следующий вид:

01,Title,Ran So Hard the Sun Went Down
02,Title,Honky Tonk Heroes (Like Me)

то вызов функции condense_csv():
condense_csv('data.csv', id_name='ID')
должен был бы создать файл condensed.csv со следующим содержанием:

ID,Title
01,Ran So Hard the Sun Went Down
02,Honky Tonk Heroes (Like Me)

Примечание 2.
Гарантируется, что в передаваемом в функцию csv файле разделителем является запятая, при этом кавычки
не используются.
Примечание 3.
При открытии файла используйте явное указание кодировки UTF-8.


##################
ball,color,purple
ball,size,4
ball,notes,it's round
cup,color,blue
cup,size,1
cup,notes,none
##################

object,color,size,notes
ball,purple,4,it's round
cup,blue,1,none

"""


def condense_csv(filename: str, id_name='ID'):
    with open(filename, encoding='UTF-8') as f:
        data = {}
        for row in f:
            id_n, col1, col2 = row.strip().split(',')
            data[id_n] = data.get(id_n, {}) | {col1: col2}

    header = [id_name] + [list(s.keys()) for s in data.values()][0]

    with open('condensed.csv', 'w', encoding='UTF-8', newline='') as f_out:
        f_out.write(','.join(header) + '\n')
        for k, v in data.items():
            f_out.write(f"{k},{','.join(list(v.values()))}\n")


condense_csv('d.csv')

# import csv
#
#
# def condense_csv(filename, id_name):
#     with open(filename, encoding='utf-8') as file:
#         objects = {}
#         for obj, attr, value in csv.reader(file):
#             if obj not in objects:
#                 objects[obj] = {id_name: obj}
#             objects[obj][attr] = value
#
#     with open('condensed.csv', 'w', encoding='utf-8') as file:
#         writer = csv.DictWriter(file, fieldnames=objects[obj])
#         writer.writeheader()
#         writer.writerows(objects.values())

# через pandas
# import pandas as pd
#
#
# def condense_csv(file_name, id_name='ID'):
#     df = pd.read_csv(file_name, delimiter=',', header=None, dtype=str)
#     pt = df.pivot(index=0, columns=1, values=2)
#     pt[list(df[1].drop_duplicates())].to_csv('condensed.csv', encoding='utf-8', index_label=id_name)
#
#
# condense_csv('d.csv')
