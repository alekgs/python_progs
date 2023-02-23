"""
Ваша задача создать функцию-генератор my_range_gen, которая копирует работу range.
    my_range_gen можно запускать, передав ей один параметр stop
    my_range_gen(stop)
    и она должна генерировать последовательность от 0 до stop не включительно

    for i in my_range_gen(5):
        print(i)

    # Будет напечатано
    # 0
    # 1
    # 2
    # 3
    # 4

   my_range_gen можно запускать, передав ей два параметра start и stop
   my_range_gen(start, stop)

    и она должна генерировать последовательность от start включительно до stop не включительно
    for i in my_range_gen(4, 8):
        print(i)

    # Будет напечатано
    # 4
    # 5
    # 6
    # 7

    my_range_gen можно запускать, передав ей три параметра start, stop и step
    my_range_gen(start, stop, step)
    и она должна генерировать последовательность от start включительно до stop не включительно c шагом step

    for i in my_range_gen(4, 8, 2):
        print(i)

    # Будет напечатано
    # 4
    # 6

    for i in my_range_gen(8, 5, -1):
        print(i)

    # Будет напечатано
    # 8
    # 7
    # 6

    предусмотрите вариант запуска my_range_gen со значением step = 0. При таком варианте вызова, функция не должна
    генерировать ни одной последовательности и закончить свою работу. Такое же поведение должно быть если переданы
    нелогичные значения start, stop и step(см. примеры)

    for i in my_range_gen(4, 8, 0):
        print(i)
    # Ничего не печатает

    for i in my_range_gen(20, 10, 3):
        print(i)
    # Ничего не печатает, потому что нельзя пройти от 20 до 10 с шагом 3


    for i in my_range_gen(1, 10, -2):
        print(i)
    # Ничего не печатает, потому что нельзя пройти от 1 до 10 с шагом -2
"""

# def my_range_gen(start, stop=None, step=1):
#     if stop is None:
#         stop, start = start, 0
#     while step and (start < stop, start > stop)[step < 0]:
#         yield start
#         start += step

from typing import Generator


def my_range_gen(*args) -> Generator[int, int, None]:
    """Принимает аргументы и генерирует последовательность"""
    len_args = len(args)
    start, stop, step = 0, 0, 1

    if len_args > 3 or len_args == 0:
        raise TypeError("Error in number of arguments")

    match len_args:
        case 1:
            stop = args[0]
        case 2:
            start, stop = args
        case 3:
            start, stop, step = args

    while step and (start > stop, start < stop)[step > 0]:
        yield start
        start += step


for i in my_range_gen(10):
    print(i)
