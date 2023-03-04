"""
Функция print_bar_chart()

Реализуйте функцию print_bar_chart(), которая принимает два аргумента в следующем порядке:

    data — строка или список строк
    mark — одиночный символ

Функция должна определять:

    сколько раз встречается каждый символ в строке, если data является строкой
    сколько раз встречается каждая строка в списке, если data является списком

Затем функция должна выводить результат в виде столбчатой диаграммы, указывая каждый символ (строку) и его
количество. Количество отображается как повторение символа mark соответствующее число раз, например, если mark='+',
то количество, равное четырем, будет отображено как ++++. Символы (строки) в диаграмме должны быть расположены в
порядке уменьшения количества, при равных количествах — в своем исходном порядке, каждая на отдельной строке,
в следующем формате:

<символ или строка> |<количество>

Примечание 1.
Обратите внимание на второй тест, функция должна добавлять нужное количество пробелов,
если строка имеет меньшую длину, чем другие.

Примечание 2.
Программа должна учитывать регистр. То есть, например, строки Python и python считаются различными.
"""

from collections import Counter
# from matplotlib import pyplot as plt


def print_bar_chart(data, mark):
    data = Counter(data)
    max_l = len(max(data, key=len))
    for name, cnt in data.most_common():
        print(f'{name:{max_l}} |{mark * cnt}')

    # # data = sorted(Counter(data).items(), key=lambda x: (x[1], x[0]))
    # data = Counter(data).most_common()
    # groups = [d[0] for d in data]
    # counts = [d[1] for d in data]
    # print(groups)
    # print(counts)
    # # plt.barh([d[0] for d in data], [d[1] for d in data])
    # plt.barh(groups, counts)
    # plt.show()


# tests

# print_bar_chart('beegeek', '+')

"""
e |++++
b |+
g |+
k |+
"""

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')

"""
java      |####
C++       |###
pascal    |##
python    |#
assembler |#
C         |#
"""
