"""
Напишите функцию file_n_lines, которая печатает первые n-строка файла.
Функция file_n_lines принимает на вход название файла и количество строк для прочтения.
Не забывайте избавляться от символа переноса строки
К примеру, если бы имелся файл hello.txt со следующим содержимым:
h
he
hel
hell
hello
то вызов file_n_lines(hello.txt, 3) должен распечатать следующее:
h
he
hel

"""


def file_n_lines(f_name: str, n: int) -> None:
    """Функция принимает на вход название файла, количество строк для прочтения и выводит их"""
    try:
        f = open(f_name, 'r', encoding='utf-8')
        [print(f.readline().strip()) for _ in range(n)]
        f.close()
    except IOError as e:
        print(e)
        return


try:
    file_n_lines('111.txt', 4)
except TypeError as ee:
    print(ee)
