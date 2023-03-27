"""
Вводится текст со сбалансированными скобками, требуется вывести на экран содержимое скобок (на отдельных строках).
На пробелы и знаки препинания внимание не обращать, вложенных скобок в исходной строке нет.
Текст состоит из слов, записанных латинскими буквами через пробел, знаков препинания.

Скобка считается сбалансированной (корректной), если у каждой открывающей скобки есть соответствующая ей закрывающая
скобка. Закрывающая скобка не идёт впереди открывающей.
Пример
Ввод
When (he saw Sally) (a girl he used to go to school with) in the shop, (he could not believe) his eyes. She was fantastic (as always)!

Вывод
a girl he used to go to school with
as always
"""
# import re
#
# Регулярка для условия задачи
# regex = r"\((.*)\)"

# получить список слов из строки string
# nums = re.findall(r'(\w+)', string)

# nums = re.findall(r'\((?:.*)\)', string, flags=re.S)
# nums = re.search(r'\((.*)\)', string, flags=re.S)[0]

# nums = [i for i in nums]
# print(nums)



string = input()

# количество открывающих скобок
count = string.count('(')

# индекс первого вхождения '(' и ')'
start = string.find('(')
end = string.find(')')

for i in range(count):
    # вывод содержимого между скобок
    print(string[start + 1:end])
    # сдвиг начальной позиции для поиска
    start = string.find('(', end + 1)
    end = string.find(')', end + 1)
