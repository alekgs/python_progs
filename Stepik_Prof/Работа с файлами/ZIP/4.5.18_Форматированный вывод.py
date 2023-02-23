"""
Форматированный вывод

Вам доступен архив workbook.zip, содержащий различные папки и файлы. Напишите программу, которая выводит названия
всех файлов из этого архива в лексикографическом порядке, указывая для каждого его дату изменения, а также объем до и
после сжатия, в следующем формате:

<название файла>
  Дата модификации файла: <дата изменения>
  Объем исходного файла: <объем до сжатия> байт(а)
  Объем сжатого файла: <объем после сжатия> байт(а)

Между данными о двух файлах должна располагаться пустая строка.

Примечание 1. Если файл находится в папке, вывести следует только название без пути.
Примечание 2. Начальная часть ответа выглядит так (в качестве отступов используйте два пробела):

Alexandra Savior – Crying All the Time.mp3
  Дата модификации файла: 2021-11-30 13:27:02
  Объем исходного файла: 5057559 байт(а)
  Объем сжатого файла: 5051745 байт(а)

Hollow Knight Silksong.exe
  Дата модификации файла: 2013-08-22 08:20:06
  Объем исходного файла: 805992 байт(а)
  Объем сжатого файла: 494930 байт(а)

"""
from zipfile import ZipFile
from datetime import datetime as dt

# result = []
# with ZipFile('workbook.zip') as zip_file:
#     for i in zip_file.infolist():
#         if not i.is_dir():
#             f_name = i.filename.split('/')[-1]
#             result.append([f_name, dt(*i.date_time), i.file_size, i.compress_size])
#
# for s in sorted(result):
#     s_out = ''
#     s_out += f'{s[0]}\n'
#     s_out += f'  Дата модификации файла: {s[1]}\n'
#     s_out += f'  Объем исходного файла: {s[2]} байт(а)\n'
#     s_out += f'  Объем сжатого файла: {s[3]} байт(а)\n'
#     print(s_out)

with ZipFile('workbook.zip') as zip_file:
    info_files = filter(lambda x: not x.is_dir(), zip_file.infolist())

    for i in sorted(info_files, key=lambda x: x.filename.rsplit('/')[-1]):
        print(i.filename.split('/')[-1])
        print('  Дата модификации файла:', dt(*i.date_time))
        print('  Объем исходного файла:', i.file_size, 'байт(а)')
        print('  Объем сжатого файла:', i.compress_size, 'байт(а)\n')

