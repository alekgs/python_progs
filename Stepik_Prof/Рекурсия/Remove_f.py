"""
Напишите рекурсивную функцию remove_f, которая принимает на вход один аргумент - string,
строку, из которой нужно удалить все буквы ’f’ и создает новую строку, без этих символов.
"""


def remove_f(string: str):
    index = string.find('f')
    if index <= 0:
        return string
    else:
        return remove_f(string[:index] + string[index + 1:])


print(remove_f('Four furious friends fought for the phone'))
