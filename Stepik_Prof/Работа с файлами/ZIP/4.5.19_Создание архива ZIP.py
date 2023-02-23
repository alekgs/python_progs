"""
Вам доступен набор различных файлов, названия которых представлены в списке file_names.
Дополните приведенный ниже код, чтобы он создал архив files.zip и добавил в него все файлы из данного списка.

Примечание. Считайте, что файлы из списка file_names находятся в папке с программой.
"""
from zipfile import ZipFile
import os

# исходные данные
f_ext = '.py'  # расширение файлов
f_path = os.curdir


def read_files(path: str, file_ext: str):
    files_info = []
    with os.scandir(path) as it:
        for f_obj in it:
            if f_obj.is_file() and f_obj.name.endswith(file_ext):
                files_info.append(f_obj.name)
    return files_info


file_names = ['how to prove.pdf', 'fipi_demo_2022.pdf', 'Hollow Knight Silksong.exe',
              'code.jpeg', 'stepik.png', 'readme.txt', 'shopping_list.txt',
              'Alexandra Savior – Crying All the Time.mp3', 'homework.py', 'test.py']

with ZipFile('files.zip', mode='w') as zip_file:
    # for f in read_files(os.curdir, f_ext):
    [zip_file.write(f) for f in file_names]


