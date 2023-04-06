"""
Задача о рюкзаке

Вам доступен список items, содержащий набор предметов. Каждый предмет представлен в виде
именованного кортежа и имеет три параметра — название, массу (в граммах) и ценность (в рублях).
Также имеется рюкзак определённой грузоподъёмности.

Напишите программу, которая определяет, какие предметы из представленного набора следует взять,
чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом весовое
ограничение рюкзака.

Формат входных данных
На вход программе в первой строке подается число — грузоподъемность рюкзака (в граммах).

Формат выходных данных
Программа должна определить какие предметы из представленного набора
следует взять, чтобы собрать рюкзак с максимальной ценностью предметов внутри, соблюдая при этом
весовое ограничение рюкзака, и вывести названия полученных предметов в лексикографическом
порядке, каждое на отдельной строке. Если рюкзак не позволяет взять ни один предмет,
программа должна вывести текст:
Рюкзак собрать не удастся

Примечание 1.
Рюкзак не обязательно должен быть наполнен полностью.

Sample Input 1:
500

Sample Output 1:
Золотая монета
Мобильный телефон
Наушники
Обручальное кольцо
Ручка Паркер

Sample Input 2:
1

Sample Output 2:
Рюкзак собрать не удастся

Sample Input 3:
10

Sample Output 3:
Золотая монета
"""

from itertools import combinations, chain
from collections import namedtuple

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000), Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000), Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000), Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000), Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000), Item('Лимитированные кроссовки', 300, 80_000)]
#
# bag_weight = int(input())
# bag_weight = 2500
# bag_price = 0
# bag = None
#
# for i in range(1, len(items) + 1):
#     for k in set(combinations(items, i)):
#         sum_mass = sum(item.mass for item in k)
#         sum_price = sum(item.price for item in k)
#         if sum_mass <= bag_weight and sum_price > bag_price:
#             bag = k
#             bag_price = sum_price
#
# if bag:
#     print(*sorted(item.name for item in bag), sep='\n')
# else:
#     print('Рюкзак собрать не удастся')


# value = int(input())
value = 500

if min(items, key=lambda x: x.mass).mass > value:
    print('Рюкзак собрать не удастся')
else:
    data = chain.from_iterable(combinations(items, i) for i in range(1, 11))
    data_filtered = filter(lambda x: value >= sum(i.mass for i in x), data)
    result = max(data_filtered, key=lambda x: sum(i.price for i in x))

    print(*sorted(i.name for i in result), sep='\n')
