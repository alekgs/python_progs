import pandas as pd
"""
#  Рассмотрим DataFrame: 	
    A 	B 	C 	D
0 	1 	10 	11 	20
1 	2 	11 	12 	21
2 	3 	12 	13 	22
3 	4 	13 	14 	23
4 	5 	14 	15 	24

Заполните пробел, чтобы создать новый датафрейм df2, который является копией df с дополнительным столбцом 'E', 
содержащим значения [25, 26, 27, 28, 29]:

df2 = df.________(E=[25, 26, 27, 28, 29])

"""
data = {'A': list(range(1, 6)), 'B': list(range(10, 15)), 'C': list(range(11, 16)), 'D': list(range(20, 25))}
df = pd.DataFrame(data)
df2 = df.assign(E=[25, 26, 27, 28, 29])
df2 = df2.assign(F=[30, 31, 32, None, None])
# data = {'user': ['Ivan', 'Petr', 'Nikolay', 'Andrey'],
#         'time_per_page': [10, 30, 15, 5],
#         'pages': [7, 9, 12, 3]}
# result = pd.DataFrame(data)
print(df2)
