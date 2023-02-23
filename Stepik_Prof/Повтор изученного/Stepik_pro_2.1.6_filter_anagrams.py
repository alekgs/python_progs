"""
Функция filter_anagrams()

Анаграммы — это слова, которые состоят из одинаковых букв. Например:
    адаптер — петарда
    адресочек — середочка
    азбука — базука
    аистенок — осетинка

Реализуйте функцию filter_anagrams(), которая принимает два аргумента в следующем порядке:
    word — слово в нижнем регистре
    words — список слов в нижнем регистре

Функция должна возвращать список, элементами которого являются слова из списка words, которые представляют анаграмму 
слова word. Если список words пуст или не содержит анаграмм, функция должна вернуть пустой список.

Примечание 1.
Слова в возвращаемом функцией списке должны располагаться в своем исходном порядке.

Примечание 2. 
Считайте, что слово является анаграммой самого себя.

word = 'abba'
anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
print(filter_anagrams(word, anagrams))
 ['aabb', 'bbaa']

Sample Input 2:
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
 ['сеточка', 'стоечка', 'тесачок', 'чесотка']

Sample Input 3:
print(filter_anagrams('tommarvoloriddle', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
 ['iamlordvoldemort']

Sample Input 4:
print(filter_anagrams('стекло', []))
 []


"""


# # Решение 1
# def filter_anagrams(word: str, words: list) -> list or None:
#     """
#     Возвращает список, элементами которого являются слова из списка words,
#     которые представляют анаграмму слова word.
#     """
#     s1, word_len, s_out = {i: word.count(i) for i in set(word)}, len(word), []
#     for s in words:
#         if len(s) == word_len:
#             s2 = {i: s.count(i) for i in set(s)}
#             if s2 == s1:
#                 s_out.append(s)
#     return s_out
#

# # Решение 2
# def filter_anagrams(word, anagrams):
#     word = sorted(word)
#     return list(filter(lambda x: sorted(x) == word, anagrams))


# Решение 3
def filter_anagrams(word, anagrams):
    word = sorted(word)
    return [a for a in anagrams if sorted(a) == word]


# Тесты
print(filter_anagrams('abba', ['aabb', 'adcd', 'bbaa', 'dada']))
print(filter_anagrams('отсечка', ['сеточка', 'стоечка', 'тесачок', 'чесотка']))
print(
    filter_anagrams('iamlordvoldemort', ['iamlordvoldemort', 'iamdevolremort', 'mortmortmortmort', 'remortvolremort']))
print(filter_anagrams('стекло', []))
