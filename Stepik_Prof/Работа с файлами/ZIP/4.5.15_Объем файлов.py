"""
Объем файлов

Вам доступен архив workbook.zip, содержащий различные папки и файлы.
Напишите программу, которая выводит суммарный объем файлов этого архива в сжатом и не сжатом видах в байтах,
в следующем формате:

Объем исходных файлов: <объем до сжатия> байт(а)
Объем сжатых файлов: <объем после сжатия> байт(а)

Примечание 1. Вывод на примере архива test.zip из конспекта:

Объем исходных файлов: 7810260 байт(а)
Объем сжатых файлов: 7798267 байт(а)
"""
from zipfile import ZipFile

with ZipFile('workbook.zip') as zip_file:
    total_size, total_compression_size = 0, 0
    for i in zip_file.infolist():
        total_size += i.file_size
        total_compression_size += i.compress_size
print(f'Объем исходных файлов: {total_size} байт(а)')
print(f'Объем сжатых файлов: {total_compression_size} байт(а)')
