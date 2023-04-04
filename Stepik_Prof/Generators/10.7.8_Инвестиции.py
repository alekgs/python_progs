"""
Инвестиции

Вам доступен файл data.csv, который содержит информацию об инвестициях в различные стартапы. В
первом столбце записано название компании (стартапа), во втором — инвестируемая сумма в долларах,
в третьем — раунд инвестиции:

company,raisedAmt,round
LifeLock,6850000,b
LifeLock,6000000,a
LifeLock,25000000,c
MyCityFaces,50000,seed
Flypaper,3000000,a
...

Напишите программу с использованием конвейеров генераторов, определяющую общую сумму,
которая была инвестирована в раунде а, и выводящую полученный результат.

Пример вывода:
86900000000

"""
with open('data.csv', encoding='utf-8') as f:
    rows = (row for row in f)
    row_values = (row.rstrip().split(',') for row in rows)
    headers = next(row_values)
    row_dicts = (dict(zip(headers, data)) for data in row_values)
    result = (int(row['raisedAmt']) for row in row_dicts if row['round'] == 'a')
    print(sum(result))
