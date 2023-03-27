"""
Вводится строка и набор чисел, а потом строка "стоп".
Выведи все буквы, которые соответствуют индексам - введенным числам.

Пример 1
Ввод
apple
2
4
стоп

Вывод
p
e
"""

word, num = input(), input()
digits = ''
while num != 'стоп':
    digits += num
    num = input()
for i in digits:
    print(word[int(i)])
