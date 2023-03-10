"""
На вход подается строка, содержащая целые числа, записанные через пробел. Требуется превратить строку в список и
преобразовать его, вставив число ноль после всех элементов, кратных своему индексу. Необходимо вывести элементы
преобразованного списка через пробел.
Пример
Ввод
1 2 3 3 1 5 1 7
Вывод
[1, 2, 0, 3, 3, 0, 1, 5, 0, 1, 7, 0]
"""
result = []
for i, n in enumerate(map(int, input().split())):
    # добавляем число в список
    result.append(n)
    # проверка, что индекс не равен 0,
    # иначе будет ошибка - деление на 0
    if i != 0:
        # если число кратно индексу, то добавляем 0 в список
        if n % i == 0:
            result.append(0)
    # если первый элем. списка n = 0 и индекс списка i = 0
    # то также добавляем 0
    elif i == 0 and n == 0:
        result.append(0)
print(result)
