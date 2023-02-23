"""
Анаграмма
Cтрока S1 называется анаграммой строки S2, если она получается из S2 перестановкой символов.
Программа получает на вход две строки S1 и S2. Если строка S1 является анаграммой строки S2 нужно вывести YES,
в противном случае - NO
"""
a, b = input(), input()

s1 = {i: a.count(i) for i in set(a) if not i.isalpha}
s2 = {i: b.count(i) for i in set(b) if not i.isalpha}

'''
for i in a:
    if i.isalpha():
        s1[i] = s1.get(i, 0) + 1

for i in b:
    if i.isalpha():
        s2[i] = s2.get(i, 0) + 1
'''
print('YES' if s1 == s2 else 'NO')

