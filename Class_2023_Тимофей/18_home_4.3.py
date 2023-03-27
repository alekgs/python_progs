"""
Вводится список натуральных чисел через пробел. Требуется составить список (элементы списка - числа, не строки!)
из минимального элемента, его номера (первое вхождение) и сколько раз он встретился и максимального элемента,
его номера (первое вхождение) и сколько раз он встретился.

Пример
Ввод
1 2 1 4 9 5 1 9
Вывод
[1, 0, 3, 9, 4, 2]
"""
s = list(map(int, input().split()))

n_min = min(s)
n_min_index = s.index(n_min)
n_min_count = s.count(n_min)

n_max = max(s)
n_max_index = s.index(n_max)
n_max_count = s.count(n_max)

result = [n_min, n_min_index, n_min_count, n_max, n_max_index, n_max_count]
print(result)
