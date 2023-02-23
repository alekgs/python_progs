
import os
# исходные данные
files_ext = '.txt'              # расширение файлов
path_files = 'files'            # каталог, в котором лежат файлы с files_ext
merged_file = 'file_new.txt'    # результирующий файл


def read_files(path: str = os.curdir, file_ext: str = '.txt') -> dict or None:
    """Возвращает словарь из списка файлов с расширением file_ext в каталоге path"""
    files_info = {}
    # сканируем файлы в каталоге path (по умолчанию текущий каталог - os.curdir)
    with os.scandir(path) as it:
        for f_obj in it:
            if f_obj.is_file() and f_obj.name.endswith(file_ext):
                with open(os.path.join(path, f_obj.name), encoding='utf-8') as file:
                    # считаем кол-во строк в каждом файле и заносим в словарь
                    files_info[f_obj.name] = sum([1 for n in file])
    return files_info


files = read_files(path_files, files_ext)

# создаем результирующий файл в том же каталоге, где лежат исходные файлы
with open(f'{path_files}/{merged_file}', 'w', encoding='utf-8') as f_out:
    # цикл по сортированному словарю (по числу строк)
    for f_name, n_str in sorted(files.items(), key=lambda s: s[1]):
        # пишем в результирующий файл имя файла и число строк в нем
        f_out.write(f'{f_name}\n{str(n_str)}\n')
        # открываем файл из словаря и пишем его содержимое в результирующий файл
        with open(f_name, encoding='utf-8') as f_in:
            [f_out.writelines(line) for line in f_in]



