"""
Вводится сообщение. Нужно сформировать новое сообщение, в котором отсутствует самое короткое слово,
оканчивающееся на символ «e» (первое вхождение).
Сообщение состоит из слов, записанных латинскими буквами через пробел.
Пример
Ввод
The trouble with programmers is that you can never tell what a programmer is doing until it’s too late

Вывод
trouble with programmers is that you can never tell what a programmer is doing until it’s too late
"""

string, result = input(), []
# находим все слова заканчивающиеся на 'e'
# и добавляем их в список result
for w in string.split():
    if 'e' in w[-1]:
        result.append(w)
print(result)

# находим мин. длину слова в списке result
min_len = len(min(result, key=len))

# Для всех слов минимальной длины
# в цикле проверяем длину каждого слова и если она равна минимальной min_len,
# то заменяем это слово на '' в исходной строке string, добавив пробел к
# этому слову и убрав концевые пробелы (strip)
# for s in result:
#     if len(s) == min_len:
#         string = string.replace(s + ' ', '').strip()


# создаем список минимальных слов в порядке их нахождения в строке
res = [s for s in result if len(s) == min_len]
print(res)

# в string заменяем первое слово из списка на ''
print(string.replace(res[0] + ' ', '').strip())
