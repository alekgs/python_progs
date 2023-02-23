"""
Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде.
Вверху хотим видеть самые дорогие товары, внизу самые дешевые.
Программа будет принимать строки, в которых сперва указывается название товара,
а затем через двоеточие с пробелом его цена - целое положительное число.
Строка "конец" означает списка товаров и соответственно окончание ввода
Все товары имеют уникальные названия, цены не дублируются.
Ваша задача вывести список товаров по уменьшению цены

Sample Input:
Sony PlayStation 5: 46000
Телевизор QLED Samsung QE65Q60TAU: 87090
Смартфон Samsung Galaxy A11: 10000
Планшет Samsung Galaxy Tab S6: 26600
конец

Sample Output:
Телевизор QLED Samsung QE65Q60TAU
Sony PlayStation 5
Планшет Samsung Galaxy Tab S6
Смартфон Samsung Galaxy A11
"""
#
# sl = {'Sony PlayStation 5': 46000,
#       'Телевизор QLED Samsung QE65Q60TAU': 87090,
#       'Планшет Samsung Galaxy Tab S6': 26600,
#       'Смартфон Samsung Galaxy A11': 10000}

sl = {}
for i in iter(input, 'конец'):
    items = i.split(': ')
    sl[items[0]] = int(items[1])

[print(k, v) for k, v in sorted(sl.items(), key=lambda item: -item[1])]

# Способ № 2
# [print(j[0]) for j in sorted((i.split(': ') for i in iter(input, 'конец')), key=lambda x: -int(x[1]))]
