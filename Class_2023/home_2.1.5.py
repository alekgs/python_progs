"""
Вводится текст, содержащий запятые и точки, программа исправляет исходный текст, добавляя, если нужно пробел после
точки или запятой. Пробел в конце текста не ставится.

Привет,как дела.
Привет, как дела.

eqlbahbovv, pzpumhz, mlcgtbbnfr
eqlbahbovv, pzpumhz, mlcgtbbnfr

Moscow.Petersburg.Novgorod.Kaluga
Moscow. Petersburg. Novgorod. Kaluga

Moscow.Petersburg,Novgorod,Kaluga.
Moscow. Petersburg, Novgorod, Kaluga.

"""

string = input()
start, word_list = 0, []

for i in range(len(string)-1):
    if string[i] == '.' or string[i] == ',':
        word_list.append(string[start:i+1].strip())
        start = i + 1
    if i == len(string) - 2:
        word_list.append(string[start:].strip())
print(' '.join(word_list))
