"""
Задача №3
В папке лежит некоторое количество файлов.
Считайте, что их количество и имена вам заранее известны

Необходимо объединить их в один по следующим правилам:

- Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них
(то есть первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
- Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

Пример Даны файлы: 1.txt

Строка номер 1 файла номер 1
Строка номер 2 файла номер 1

2.txt
Строка номер 1 файла номер 2

Итоговый файл:

2.txt
1
Строка номер 1 файла номер 2
1.txt
2
Строка номер 1 файла номер 1
Строка номер 2 файла номер 1

"""

file_path = 'files/'
file_list, f_out = ['1.txt', '2.txt', '3.txt'], 'merged_file.txt'
file_info = {}
for file in file_list:
    with open(file_path + file, encoding='utf-8') as f:
        file_info[f.name] = sum([1 for n in f])

with open(file_path + f_out, 'w', encoding='utf-8') as f_merged:
    for f_name, num_lines in sorted(file_info.items(), key=lambda s: s[1]):
        f_merged.write(f'{f_name}\n{str(num_lines)}\n')
        with open(f_name, encoding='utf-8') as f_in:
            [f_merged.writelines(line) for line in f_in]

