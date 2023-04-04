"""
Функция nonempty_lines()

Реализуйте генераторную функцию nonempty_lines(), которая принимает один аргумент:
    file — название текстового файла, например, data.txt

Функция должна возвращать генератор, порождающий последовательность всех непустых строк файла
file с убранным символом переноса строки \n. Если строка содержит более 25 символов,
она заменяется многоточием ....
"""


def nonempty_lines(file):
    with open(file, encoding='utf-8') as f:
        rows = filter(len, map(str.strip, f))
        yield from ((row, '...')[len(row) > 25] for row in rows)
