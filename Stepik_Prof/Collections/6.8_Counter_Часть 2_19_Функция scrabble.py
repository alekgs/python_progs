"""
Функция scrabble()

Реализуйте функцию scrabble(), которая принимает два аргумента в следующем порядке:
    symbols — набор символов
    word — слово

Функция должна возвращать True, если из набора символов symbols можно составить слово word,
или False в противном случае.

Примечание 1.
При проверке учитывается количество символов, которые нужны для составления слова, и не учитывается их регистр.

"""

from collections import Counter


def scrabble(symbols, word):
    return Counter(symbols.lower()) >= Counter(word.lower())


# tests

print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))
# True

print(scrabble('begk', 'beegeek'))
# False

print(scrabble('beegeek', 'beegeek'))
# True
