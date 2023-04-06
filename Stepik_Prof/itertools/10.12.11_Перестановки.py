"""
Перестановки

Напишите программу, которая выводит все перестановки символов строки без дубликатов.

Формат входных данных
На вход программе подается произвольная строка из строчных латинских букв,
длина которой не превышает 10 символов.

Формат выходных данных
Программа должна вывести все перестановки символов данной строки без
дубликатов в алфавитном порядке, каждую на отдельной строке.

Sample Input 1:
aab

Sample Output 1:
aab
aba
baa

Sample Input 2:
abc

Sample Output 2:
abc
acb
bac
bca
cab
cba

Sample Input 3:
ab

Sample Output 3:
ab
ba

Sample Input 4:
a

Sample Output 4:
a
"""

from itertools import permutations

res = (''.join(i) for i in set(permutations(input())))
print(*sorted(res), sep='\n')
