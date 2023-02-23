"""
Количество файлов

Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит единственное число — количество файлов в этом архиве.

Примечание 1. Обратите внимание, что папка не считается файлом.
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    print(sum(1 for i in zip_file.infolist() if not i.is_dir()))

