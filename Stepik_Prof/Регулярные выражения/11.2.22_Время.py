"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют времена формата HH:MM.

Примечание 1.
Требуется дополнительная проверка на корректность, то есть время 54:96 не должно
соответствовать регулярному выражению regex.

Sample Input 1:
So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30 in 23:59

Sample Output 1:
17:30

Sample Input 2:
00:00, 00:60, 24:00, 50:39, 17/30

Sample Output 2:
00:00

s....k S.{4}k S....k stepik s.4k Stepik S4444k s.{4}k s4k S.4k
"""

import re

# regex = r'[0-1][\d]:[0-5]\d|2[0-3]:[0-5]\d'

regex = r'[sS].{4}k'
print(*re.findall(regex, input()))
