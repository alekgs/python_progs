"""
Новый print

Напишите программу с использованием декоратора, которая переопределяет функцию print() так,
чтобы она печатала весь текст в верхнем регистре.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна задекорировать функцию print() так, чтобы она печатала весь текст в верхнем регистре.

Примечание 1. Значения sep и end также должны переводиться в верхний регистр.



В функции-обертке, нужно сделать новый кортеж args и словарь kwargs со строчными заглавными
значениями, и вызвать нашу функцию с измененными args и kwargs.

На выходе вручную декорируем print
print = new_print(print)


"""


# def dec(func):
#     def wrapper(*args, **kwargs):
#         print('Аргументы: ', args, 'Тип: ', type(args))
#         print('Именованные аргументы: ', kwargs, 'Тип: ', type(kwargs))
#         func(*args, **kwargs)
#     return wrapper
# new_print = dec(print)
# new_print('bee', 'geek', sep='***', end='_LINEEND')


def new_print(func):
    def wrapper(*args, **kwargs):
        args = list(map(str.upper, map(str, args)))
        kwargs = {k: v.upper() for k, v in kwargs.items()}
        func(*args, **kwargs)
    return wrapper


print = new_print(print)

# Sample Input 1:
print('hi', 'there', end='!')

# Sample Output 1:
# HI THERE!

# Sample Input 2:
print('are you in trouble?')

# Sample Output 2:
# ARE YOU IN TROUBLE?

# Sample Input 3:
print(111, 222, 333, sep='xxx')

# Sample Output 3:
# 111XXX222XXX333
