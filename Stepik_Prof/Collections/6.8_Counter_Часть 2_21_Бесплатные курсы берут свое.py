"""
Бесплатные курсы берут свое 😢

Для дополнительного заработка Тимур решил заняться продажей овощей.
У него имеются данные о продажах за год, разделенные на четыре файла по кварталам: quarter1.csv, quarter2.csv,
quarter3.csv и quarter4.csv. В каждом файле в первом столбце указывается название продукта,
а в последующих — количество проданного продукта в килограммах за определенный месяц:

продукт,январь,февраль,март
Картофель,39,61,3
Дайкон,51,96,83
...

Также присутствует файл prices.json, содержащий словарь, в котором ключом является название продукта,
а значением — цена за килограмм в рублях:

{
   "Картофель": 53,
   "Дайкон": 55,
...
}

Напишите программу, которая выводит единственное число —
сумму, заработанную Тимуром за год на продаже овощей.
"""
import csv
import json
import pandas as pd
from time import perf_counter as pf
from collections import Counter

# Counter
# #1
start = pf()
cnt = Counter()
for n in '1234':
    with open(f'quarter{n}.csv', encoding='UTF-8') as f:
        __, *rows = csv.reader(f)
        [cnt.update({key: sum(map(int, vals))}) for key, *vals in rows]

with open('prices.json', encoding='utf-8') as file:
    prices = json.load(file)

print(sum(prices[key] * val for key, val in cnt.items()))
end = pf() - start
print('solution #1 (Collections Counter) - elapsed time: ', end)

# Дмитрий Гудков
# #2
start = pf()
with open('prices.json', encoding='utf-8') as price:
    prices, total = json.load(price), 0
    for i in '1234':
        with open(f'quarter{i}.csv', encoding='utf-8') as file:
            __, *quarter = csv.reader(file)
            for p in quarter:
                total += prices[p[0]] * sum(map(int, p[1:]))
    print(total)

end = pf() - start
print('solution #2 (Дмитрий Гудков)- elapsed time: ', end)


# Pandas
# #3
# start = pf()
start = pf()

df = [pd.read_csv(f'quarter{i}.csv') for i in '1234']
data = pd.concat(df, axis=1).set_index('продукт')
prices = pd.read_json('prices.json', typ='series')
data.index = prices.index

end = pf() - start
print((data.sum(axis=1) * prices).sum())


print('solution #3 (Pandas) - elapsed time: ', end)

