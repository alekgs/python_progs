"""
Наилучший показатель

Вам доступен архив workbook.zip, содержащий различные папки и файлы.

Напишите программу, которая выводит название файла из этого архива,
который имеет наилучший показатель степени сжатия.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Гарантируется, что в исходном архиве только один файл имеет наилучший показатель степени сжатия.
"""
from zipfile import ZipFile
result = []
with ZipFile('workbook.zip') as zip_file:
    for i in zip_file.infolist():
        if not i.is_dir() and i.compress_size < i.file_size:
            result.append((i.filename.split('/')[-1], i.compress_size/i.file_size))
print(min(result, key=lambda s: s[1])[0])

