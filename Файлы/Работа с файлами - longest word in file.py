"""
Напишите функцию longest_word_in_file, которая принимает имя файла и внутри его содержимого находит самое длинное
слово и возвращает его в качестве ответа. В случае,  если есть несколько слов с максимальной длиной, нужно вернуть
слово, которое встречается последнее в тексте. При этом слова в тексте отделяются друг от друга пробелами,
любые другие знаки пунктуации необходимо исключить.  И также учитывайте, что слова в тестах будут как на русском
языке, так и на английском.

Если бы содержимое файла было таким:
He was running, but it was like running through deep water. There were trees all around him,
trees which tried to stop him. They reached out with their branches.
And it was behind him. It was coming nearer.

то ответом было бы слово branches

Все возможные знаки пунктуации можно получить из модуля string
from string import punctuation
"""

from string import punctuation as pnc


def longest_word_in_file(file_name: str) -> str or None:
    """Принимает имя файла и внутри его содержимого находит самое длинное слово и возвращает его в качестве ответа"""
    f = open(file_name, encoding='utf-8')
    longest_word = sorted(map(lambda s: s.strip(pnc), f.read().split()), key=len)[-1]
    f.close()
    return longest_word


# max([i.strip((punctuation)) for i in f.read().split()][::-1], key=len)
# max(arr[::-1], key=len)
#
# for i in map(int, f.read().splitlines()):
#     if i in range(100, 1000):
#         count_3x += 1
#     elif i in range(10, 100):
#         sum_2x += i


print(longest_word_in_file('1111.txt'))
