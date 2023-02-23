"""
Сортировка 2 введенных списков и вывод 1 отсортированного по возрастанию
"""

# Способ 1 -  сортировка слиянием
"""
def sort_list(l1, l2):  
    l_new = []
    while min(len(l1), len(l2)) > 0:
        if l1[0] > l2[0]:
            to_insert = l2.pop(0)
            l_new.append(to_insert)
        elif l1[0] <= l2[0]:
            to_insert = l1.pop(0)
            l_new.append(to_insert)
    if len(l1) > 0:
        for i in l1:
            l_new.append(i)
    if len(l2) > 0:
        for i in l2:
            l_new.append(i)
    return l_new
"""

# Способ 2 - через min()
a, b = map(int, input().split())
lst = list(map(int, input().split())) + list(map(int, input().split()))
result = []

while len(lst) != 0:
    a = min(lst)       # минимальный элемент в списке
    result.append(a)   # добавим элемент в новый список
    lst.remove(a)      # удалим элемент из старого списка

print(*result)

# result = sort_list(lst1, lst2)
# print(*result)
