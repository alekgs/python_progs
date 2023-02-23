"""
Файлы в файле 🌶️🌶️

Вам доступен текстовый файл files.txt, содержащий информацию о файлах.
Каждая строка файла содержит три значения, разделенные символом пробела
— имя файла, его размер (целое число) и единицы измерения:

cant-help-myself.mp3 7 MB
keep-yourself-alive.mp3 6 MB
bones.mp3 5 MB
...
Напишите программу, которая группирует данные файлы по расширению, определяя общий объем файлов каждой группы,
и выводит полученные группы файлов, указывая для каждой ее общий объем. Группы должны быть расположены в
лексикографическом порядке названий расширений, файлы в группах — в лексикографическом порядке их имен.

Примечание 1. Например, если бы файл files.txt имел вид:
input.txt 3000 B
scratch.zip 300 MB
output.txt 1 KB
temp.txt 4 KB
boy.bmp 2000 KB
mario.bmp 1 MB
data.zip 900 MB

то программа должна была бы вывести:
boy.bmp
mario.bmp
----------
Summary: 3 MB

input.txt
output.txt
temp.txt
----------
Summary: 8 KB

data.zip
scratch.zip
----------
Summary: 1 GB

где Summary — общий объем файлов группы.

Примечание 2. Гарантируется, что все имена файлов содержат расширение.
Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных)
единицах измерения с округлением до целых. Другими словами, сначала следует определить суммарный объем
всех файлов группы, скажем, в байтах, а затем перевести полученное значение в самые крупные (максимально возможные)
единицы измерения.

Примеры перевода:
    1023 B -> 1023 B
    1300 B -> 1 KB
    1900 B -> 2 KB

Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:

    1 KB = 1024 B
    1 MB = 1024 KB
    1 GB = 1024 MB

"""
from math import floor, log

units = {'B': 1, 'KB': 1024, 'MB': 1024 ** 2, 'GB': 1024 ** 3}
f_list = {}


def get_unit_name(size: int) -> str:
    """Принимает число в байтах и возвращает число в B, KB, MB, GB"""
    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')
    pwr = floor(log(size, 1024))
    return f'{size / 1024 ** pwr:.0f} {unit_names[pwr]}'


with open('files.txt', encoding='utf-8') as file:
    for s in file:
        f = s.split()
        f_name, f_ext = f[0].split('.')
        f_size = int(f[1]) * units.get(f[2])
        f_list[f_ext] = f_list.get(f_ext, {}) | {f_name: f_size}

for k, v in sorted(f_list.items()):
    [print(f'{s}.{k}') for s in sorted(v.keys())]
    print('-' * 10)
    total_size = sum(i for i in v.values())
    print(f'Summary: {get_unit_name(total_size)}')
    print()
