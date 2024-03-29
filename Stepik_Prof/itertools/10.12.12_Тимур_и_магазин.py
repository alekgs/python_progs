"""
Тимур пришел в книжный магазин, чтобы приобрести новую книгу по математике, стоимость которой
равна 100$. У него в кошельке имеется множество купюр различного номинала, которые
представлены в списке wallet. Например, Тимур может расплатиться одной купюрой в 100$ или
двумя по 50$.

Дополните приведенный ниже код, чтобы он вывел количество способов, которыми Тимур может
приобрести книгу стоимостью 100$.

Примечание. Способы расплатиться наборами купюр вида 50,20,20,10 и 20,10,50,20 считаются
одинаковыми и не должны учитываться повторно.

Cначала создаётся последовательность различных
комбинаций, из неё отбираются те, сумма элементов которой равна 100, и добавляется в список длина
отфильтрованной последовательности.  Сначала создаются комбинации по 1 элементу, потом по двум,
потом по трём и т.д. На самом деле, это чистая случайность, что ответ совпал с длиной списка,
потому что, по сути, это неправильно. Нужно считать сумму элементов этого списка, а не его длину.
Например, был бы у нас список длиной 5. На первой итерации у нас получилось 3 совпадения,
на второй 0, на третьей 5, на 4 и 5 тоже 0. Ответ должен был бы получиться 3 + 0 + 5 + 0 + 0 = 8.
"""

from itertools import combinations

wallet = [100, 100, 50, 50, 50, 50, 20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]

count = 0
for i in range(1, len(wallet)):
    count += sum(1 for k in set(combinations(wallet, r=i)) if sum(k) == 100)
print(count)

# res = set()
# for i in range(1, len(wallet)):
#     for k in combinations(wallet, r=i):
#         if sum(k) == 100:
#             res.add(k)
# print(len(res))