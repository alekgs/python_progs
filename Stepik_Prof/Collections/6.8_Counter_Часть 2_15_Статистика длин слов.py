"""
Статистика длин слов

Дана последовательность слов. Напишите программу, которая группирует слова из этой последовательности по их длине и
определяет количество слов в каждой полученной группе.

Формат входных данных
На вход программе подается последовательность слов, разделенных пробелом.

Формат выходных данных
Программа должна сгруппировать слова из введенной последовательности по их длине и определить
количество слов в каждой полученной группе. Каждую группу характеризуют два числа — длина слов в этой группе и
количество слов в этой группе. Например, для группы {is, to, hi, no} это числа 2 и 4. Программа должна вывести данные
о каждой группе, расположив их в порядке увеличения количества слов в них, каждые на отдельной строке, в следующем
формате:

Слов длины <длина слов в группе>: <количество слов в группе>

Примечание 1.
Если две разные группы имеют равное количество слов, то первой должна следовать та группа,
слово которой в исходной последовательности встречается раньше.
"""

from collections import Counter

c = Counter([len(word) for word in input().lower().split()])
[print(f'Слов длины {s}: {c[s]}') for s in sorted(c, key=c.get)]



# tests
# Любимой песни слог Знакомый ритм слов Панацея от всего

# Слов длины 8: 1
# Слов длины 2: 1
# Слов длины 7: 2
# Слов длины 5: 2
# Слов длины 4: 3
