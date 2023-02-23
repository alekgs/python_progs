"""
Задание 3
Дан список поисковых запросов.
Получить распределение количества слов в них.
Т.е. поисковых запросов из одного слова - 5%, из двух - 7%, из трех - 3% и т.д.
"""

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

words_dict, count_queries = {}, len(queries)

for query in queries:
    count_words = len(query.split())
    words_dict[count_words] = words_dict.get(count_words, 0) + 1

print(f'Всего поисковых запросов - {count_queries}')
for key, value in words_dict.items():
    print(f'Поисковых запросов из {key} слов: {value/count_queries:.0%} ({value})')
