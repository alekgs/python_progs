"""
Пропущенные комменты 🌶️

На вход программе подается строка текста с именем текстового файла, в котором написан код на языке Python. Напишите
программу, выводящую на экран имена всех функций для которых отсутствует поясняющий комментарий. Будем считать,
что любая строка, начинающаяся со слова def и пробела, является началом определения функции. Функция содержит
комментарий, если первый символ предыдущей строки - #.

Формат входных данных
На вход программе подается строка текста, содержащая имя существующего текстового файла с кодом на языке Python.

Формат выходных данных
Программа должна вывести названия всех функций (не меняя порядка их следования в исходном
файле), каждое на отдельной строке, для которых отсутствует поясняющий комментарий.
Если все функции в файле имеют поясняющий комментарий,
то следует вывести: Best Programming Team.

Примечание 1. Если бы файл содержал код:

def powers(a):
    return a, a**2, a**3

# функция вычисляет сумму всех переданных чисел
def sum_all(*args):
    return sum(args)

def matrix():
    pass

# функция возвращает количество переданных аргументов
def count_args(*args):
    return len(args)

def mean(*args):
    total = 0.0
    count = 0  
    for i in args:
        if type(i) in (int, float):
            total += i
            count += 1
    if count == 0:
        return 0.0
    else:
        return total / count
    
def greet(name, *args):
    args = (name,) + args
    return f'Hello, {" and ".join(args)}!'

# функция вычисляет факториал переданного числа
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

то результатом будет:

powers
matrix
mean
greet

Примечание 2. Гарантируется, что в файле есть хотя бы одна функция при этом вложенных функций в файле нет. 

"""

# import re
# with open(input()) as f_in:
# with open('functions.txt', encoding='utf-8') as f_in:
#     text = re.findall(r"def\s+(\w+)\(", re.sub(r"#.*\s{1}def.*\s{1}", "", f_in.read()))
#     print('\n'.join(text) or ['Best Programming Team'])


with open('functions.txt', encoding='utf-8') as f_in:
    s, lst = f_in.readlines(), []

for i, v in enumerate(s):
    if v.startswith('def') and (i == 0 or not s[i - 1].startswith('#')):
        lst.append(v[4:v.index('(')])

print(*lst or ['Best Programming Team'], sep='\n')
