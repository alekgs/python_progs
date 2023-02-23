"""
Словарь emails содержит информацию об электронных адресах пользователей, сгруппированных по домену.
Дополните приведенный код, чтобы он вывел все электронные адреса в алфавитном порядке, каждый на отдельной строке,
в формате username@domain.
Примечание 1. Для сортировки в алфавитном порядке используйте встроенную функцию sorted(), либо списочный метод sort().
Примечание 2. Группировать электронные адреса по доменам не нужно.
"""
emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
          'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
          'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
          'yandex.ru': ['surface', 'google'],
          'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
          'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
emails_lst = []
for k, v in emails.items():
    for i in v:
        emails_lst.append(f'{i}@{k}')
print(*sorted(emails_lst), sep='\n')
# print(*sorted([i+'@'+k for k, v in emails.items() for i in v]), sep = '\n')


"""
Дополните приведенный код, чтобы в списках значений элементов словаря my_dict не было чисел, больших 20.
При этом порядок оставшихся элементов меняться не должен.
"""
#
# my_dict = {'C1': [10, 20, 30, 7, 6, 23, 90], 'C2': [20, 30, 40, 1, 2, 3, 90, 12], 'C3': [12, 34, 20, 21],
#            'C4': [22, 54, 209, 21, 7], 'C5': [2, 4, 29, 21, 19], 'C6': [4, 6, 7, 10, 55], 'C7': [4, 8, 12, 23, 42],
#            'C8': [3, 14, 15, 26, 48], 'C9': [2, 7, 18, 28, 18, 28]}
#
# for k, v in my_dict.items():
#     my_dict.update({k: [i for i in v if i <= 20]})
#
# print(my_dict)

"""Напишите функцию create_actor, которая принимает произвольное количество именованных аргументов и возвращает
словарь с характеристиками актера. Если функции create_actor не передавать никаких аргументов, то она должна
возвращать базовый словарь с ключами name, surname, age. Вот так он выглядит:

create_actor() -> {
        'name': 'Райан',
        'surname': 'Рейнольдс',
        'age': 46,
    }

Если передавать именованные параметры, которые отсутствуют в базовом словаре, они дополняются к этому словарю

create_actor(height=190, movies=['Дедпул', 'Главный герой']) => {
    'name': 'Райан',
    'surname': 'Рейнольдс',
    'age': 46,
    'height': 190,
    'movies': ['Дедпул', 'Главный герой']
}

Если передавать именованные параметры, которые совпадают с ключами базового словаря, то значения в словаре должны
заменяться переданными значениями:

create_actor(name='Jack', age=20) -> {
        'name': 'Jack',
        'surname': 'Рейнольдс',
        'age': 20,
    }
"""

# def create_actor(**kwargs) -> dict:
#     """ Функция принимает произвольное количество именованных аргументов
#     и возвращает словарь с характеристиками актера
#     """
#     dict_actor = {'name': 'Райан', 'surname': 'Рейнольдс', 'age': 46}
#     if len(kwargs):
#         dict_actor.update(kwargs)
#     return dict_actor
#
#
# print(create_actor())
# print(create_actor(height=190, movies=['Дедпул', 'Главный герой']))
# print(create_actor(name='Jack', age=20))

"""
Напишите функцию info_kwargs, которая принимает произвольное количество именованных аргументов.
Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде
пары <Ключ>=<Значения>, причем ключи должны следовать в алфавитном порядке.
Данный вызов печатает следующие строки:
    age = 33
    first_name = John
    last_name = Doe
"""

#
#
# def info_kwargs(**kwargs):
#     """ Функция info_kwargs должна распечатать именованные аргументы в каждой новой строке в виде
#     пары <Ключ>=<Значения>, причем ключи должны следовать в алфавитном порядке. """
#     # kwargs = dict(sorted(kwargs.items()))
#     for key, value in sorted(kwargs.items()):
#         print(f'{key} = {value}')
#
# #
# def info_kwargs(**kwargs):
#     """ Функция info_kwargs должна распечатать именованные аргументы
#     в каждой новой строке в виде пары <Ключ>=<Значения>, причем ключи
#     должны следовать в алфавитном порядке.
#     """
#     [print(f'{key} = {value}') for key, value in sorted(kwargs.items())]
#
#
# info_kwargs(first_name="John", last_name="Doe", age=33)

"""
Давайте теперь создадим функцию print_goods, которая печатает список покупок. На вход она будет принимать
произвольное количество значений, а товаром мы будем считать любые непустые строки. То есть числа, списки,
словари и другие нестроковые объекты вам нужно будет проигнорировать. Функция print_goods должна печатать список
товаров в виде:  Порядковый номер товара>. <Название товара> (см. пример ниже). В случае, если в переданных значениях
не встретится ни одного товара, необходимо распечатать текст <Нет товаров>

print_goods('apple', 'banana', 'orange')
Программа должна вывести следующее:
1. apple
2. banana
3. orange

print_goods(1, True, 'Грушечка', '', 'Pineapple')
Программа должна вывести следующее:
1. Грушечка
2. Pineapple

print_goods([], {}, 1, 2)
Программа должна вывести следующее:
Нет товаров
"""

#
#
# def print_goods(*args) -> None:
#     """ Функция print_goods должна печатать список товаров в виде: Порядковый номер товара>. <Название товара>.
#     В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст
#     "Нет товаров"
#     """
#     i = 0
#     for k in args:
#         if type(k) == str and len(k):
#             i += 1
#             print(f'{i}. {k}')
#     if not i:
#         print('Нет товаров')
#     return
#
#
# print_goods('apple', 'banana', 'orange')
# print_goods([], {}, 1, 2)
# print_goods(1, True, 'Грушечка', '', 'Pineapple')

# def only_one_positive(*args: int) -> bool | None:
#     """Функция принимает произвольное количество числовых аргументов
#        и возвращает True, когда из всех переданных значений только одно положительное,
#        в противном случае верните False
#        """
#     pos_num = 0
#     for i in args:
#         if i > 0:
#             pos_num += 1
#     return print(pos_num == 1)
#
#
# only_one_positive(-2, -1, 0, 1,2)  # -> False
# only_one_positive(-1, 0, -3, 5, -3)  # -> True
# only_one_positive()  # -> False

# def multiply(*args: int) -> int:
#     """Функция должна находить произведение всех переданных значений
#        и возвращать его в качестве результата """
#     result = 1
#     for i in args:
#         result *= i
#     return result
#
#
# multiply(1, 2, 3)  # => 6
# multiply(1, 3)  # => 3
# multiply(2)  # => 2
# multiply()  # => 1

# def count_args(*args):
#     return print(len(args))
#
#
# count_args(1, 2, 3)  # => 3
# count_args(1, 3)  # => 2
# count_args(2)  # => 1
# count_args()  # => 0

# def format_name_list(names):
#     len_dict = len(names)
#     if len_dict == 0:
#         return ''
#     else:
#         f_row = ''
#         for i in range(len_dict):
#             f_row += names[i]['name'] + ' и ' if i == len_dict - 2 else names[i]['name'] + ', '
#         return f_row if f_row == '' else f_row[:-2]

#     for key, values in enumerate(names):
#         if key == len_dict - 2:
#             format_row += values['name'] + ' и '
#         elif key == len_dict - 1:
#             format_row += values['name']
#         else:
#             format_row += values['name'] + ', '
# return format_row


#
# def format_name_list(a):
#     y = ''
#     for i in range(len(a)):
#         y += a[i]['name'] + ' и ' if i == len(a) - 2 else a[i]['name'] + ', '
#     return y if y == '' else y[:-2]

# assert format_name_list([]) == ''
# #
# print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Maggie'}]))
# print(format_name_list([{'name': 'Bart'}]))
# print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Maggie'}]))
# print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]))
# print(format_name_list([{'name': 'Bart'}]))
# print(format_name_list([]))
#
# def get_domain_name(url):
#     #print(url.lstrip('https://www.').split('.')[0])
#     print(url.strip('https://www.').split('.')[0])

# get_domain_name("http://google.com") # "google"
# get_domain_name("http://google.co.jp") # "google"
# get_domain_name("www.xakep.ru") # "xakep"
# get_domain_name("https://youtube.com") # "youtube"
# get_domain_name("https://www.asos.com") # "asos"
# get_domain_name("http://www.lenovo.com") # "lenovo"

#
# def factorial(n):
#     fact = 1
#     for i in range(2, n + 1):
#         fact *= i
#     return str(fact)
#
#
# def trailing_zeros(n):
#     return print((len(factorial(n))-(len(factorial(n).rstrip('0')))))

#
# def trailing_zeros(n):
#     fac = str(factorial(n))
#     count_zeros = 0
#     for i in range(len(fac) - 1, -1, -1):
#         if '0' in fac[i]:
#             count_zeros += 1
#         else:
#             break
#     return print(count_zeros)

#
# trailing_zeros(6)  # =>  1, потому что 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720
# trailing_zeros(10)  # => 2, потому что 10! = 3 628 800
# trailing_zeros(20)  # => 4, потому что 20! = 2 432 902 008 176 640 000
"""

Азотистые основания нуклеотидов ДНК

К азотистым основаниям относят аденин (A), гуанин (G), цитозин (C) и тимин (T), который входит в состав только ДНК.
Они обладают схожими структурами и химическими свойствами. Это гетероциклические органические соединения, производные
пиримидина и пурина, входящие в состав нуклеотидов. Аденин и гуанин — производные пурина, а цитозин и тимин —
производные пиримидина.

В этой задаче вам необходимо создать функцию count_AGTC, которая принимает на вход строку - последовательность ДНК,
состоящая только из символов A, G, T, C. Функция count_AGTC должна подсчитать количество каждого элемента в
переданной последовательности и вернуть кортеж из найденных четырех количеств. Порядок элементов в кортеже должен
быть именно таким A, G, T, C

count_AGTC('AGGTC') => (1, 2, 1, 1)
count_AGTC('AAAATTT') => (4, 0, 3, 0)
count_AGTC('AGTTTTT') => (1, 1, 5, 0)
count_AGTC('CCT') => (0, 0, 1, 2)

Нужно написать только определение функции count_AGTC 

"""

# def count_AGTC(dna):
#     """Да вы только посмотри на эту функцию"""
#     """Да она вообще"""
#     """ничего не делает!!!"""
#     print(tuple(dna.count(i) for i in 'AGTC'))
#
#
# count_AGTC('AGGTC')  # (1, 2, 1, 1)
# count_AGTC('AAAATTT')  # (4, 0, 3, 0)
# count_AGTC('AGTTTTT')  # (1, 1, 5, 0)
# count_AGTC('CCT')  # (0, 0, 1, 2)
#
# help(count_AGTC)

# def first_repeated_word(st: str) -> str | None:
#     """Находит первый дубль в строке"""
#     # lst = []
#     # for i in st.split():
#     #     if i in lst:
#     #         return i
#     #     lst.append(i)
#     # return 'None'
#     st = st.split()
#     for x in range(len(st)):
#         if st[x] in st[:x]:
#             return print(st[x])
#
#
# first_repeated_word("ab ca bc ab")  # => "ab"
# first_repeated_word("ab ca bc Ab cA aB bc")  # => "bc"
# first_repeated_word("ab ca bc ca ab bc")  # => "ca"
# first_repeated_word("ab ca bc")  # => None
#
# def shift_letter(letter: str, shift: int):
#     """Функция сдвигает символ letter на shift позиций"""
#     new_char = chr(((ord(letter) - ord('a') + shift) % 26) + ord('a'))
#     return new_char
#
#
# shift_letter('z', 5)    # e
# shift_letter('w', 28)   # y
# shift_letter('w', -26)  # w
# shift_letter('w', -27)  # v  - 2
# shift_letter('a', 53)   # b    - 26
