"""
Младшая сестра Фёдора - Соня пишет сочинение по литературе и отправляет файлы учительнице.

Фёдор знает, что Соня никогда не ставит заглавные буквы, так как для набора текста использует компьютер. Пока никто
не видит, Фёдор решил внести исправления в сочинение сестры и написал функцию capitalize(s), которая принимает на
вход исходную строку s и возвращает строку с восстановленными заглавными буквами.

Функция работает по следующему алгоритму:
* сделать заглавной первую букву в строке, не считая пробелы;
* сделать заглавной первую букву после точки, восклицательного или вопросительного знака, не считая пробелы.

Пример

Ввод
на этом заканчиваю свое сочинение. поставьте пятерку, Мария Ивановна! я очень старалась!

Вывод
На этом заканчиваю свое сочинение. Поставьте пятерку, Мария Ивановна! Я очень старалась!
"""


def capitalize(text):
    for sign in ('.', '!', '?'):
        text = text.replace(sign, sign + '  ')
    # to_list = text.replace('.', '.  ').replace('!', '!  ').replace('?', '?  ').split('  ')
    return ' '.join(map(lambda s: s.strip()[:1].upper() + s.strip()[1:], text.split('  ')))


# Прошел только этот вариант (((

# def capitalize(text):
#     text = list(text)
#     text[0] = text[0].upper()
#     for i in range(len(text) - 2):
#         if text[i] in '!.?':
#             text[i + 2] = text[i + 2].upper()
#
#     return ''.join(text)


# test
print(capitalize('на этом заканчиваю свое сочинение.   оставьте пятерку, Мария Ивановна!   я очень старалась!  '))