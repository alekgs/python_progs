"""
The Zen of Python

Вам доступен текстовый файл pythonzen.txt, содержащий текст на английском языке:

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
...

Напишите программу, которая определяет, сколько раз встречается каждая буква в этом тексте. Буквы и их количество
должны выводиться в лексикографическом порядке, каждая на отдельной строке, в следующем формате:

<буква>: <количество>

Примечание 1. Начальная часть ответа выглядит так:

a: 53
b: 21
...

Примечание 2. Программа не должна учитывать регистр, то есть, например, буквы a и A считаются одинаковыми.
Примечание 3. Программа должна игнорировать все небуквенные символы.
Примечание 4. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 5. При открытии файла используйте явное указание кодировки UTF-8.

"""

from collections import Counter

with open('pythonzen.txt', encoding='utf-8') as f:
    char_count = Counter(filter(str.isalpha, f.read().lower()))

    # char_count = Counter()
    # for w in f.read().lower():
    #     char_count.update(Counter(filter(str.isalpha, w)))

[print(f'{k}: {v}') for k, v in sorted(char_count.items())]


#
# goods_list = Counter(input().split(','))
# max_len = len(max(goods_list, key=len))
#
# for word, count in sorted(goods_list.items()):
#     price = sum(ord(char) for char in word if char.isalpha())
#     print(f'{word:{max_len}}: {price} UC x {count} = {price * count} UC')


# tests

# лимон,лимон,лимон,груша,банан,банан,киви,киви,киви,киви

# банан: 5387 UC x 2 = 10774 UC
# груша: 5422 UC x 1 = 5422 UC
# киви : 4316 UC x 4 = 17264 UC
# лимон: 5418 UC x 3 = 16254 UC

# рубашка,футболка,футболка,брюки,футболка,сырный соус,рубашка,носки,рубашка

# брюки      : 5425 UC x 1 = 5425 UC
# носки      : 5422 UC x 1 = 5422 UC
# рубашка    : 7574 UC x 3 = 22722 UC
# сырный соус: 10896 UC x 1 = 10896 UC
# футболка   : 8669 UC x 3 = 26007 UC

