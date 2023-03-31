"""
Итератор Alphabet 🌶️

Реализуйте класс Alphabet, порождающий итераторы, конструктор которого принимает один аргумент:
    language — код языка: ru — русский, en — английский

Итератор класса Alphabet() должен циклично генерировать последовательность строчных букв:
    русского алфавита, если language имеет значение ru
    английского алфавита, если language имеет значение en

Примечание 1. Буква ё в русском алфавите не учитывается.
"""


class Alphabet:
    def __init__(self, lang):
        self.index = -1
        self.obj = {'ru': [*map(chr, range(ord('а'), ord('я') + 1))],
                    'en': [*map(chr, range(ord('a'), ord('z') + 1))]}[lang]

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.obj):
            self.index = 0
        return self.obj[self.index]


# Sample Input 1:
ru_alpha = Alphabet('ru')
print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))

# Sample Output 1:
#
# а
# б
# в

# Sample Input 2:
en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(28)]
print(*letters)

# Sample Output 2:
# a b c d e f g h i j k l m n o p q r s t u v w x y z a b

