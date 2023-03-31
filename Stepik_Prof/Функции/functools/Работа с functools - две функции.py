"""
Две функции

Вам доступна уже реализованная функция send_email(), которая принимает три аргумента в следующем
порядке:

    name — имя
    email_address — адрес электронной почты
    text — содержание письма

Функция отправляет письмо пользователю с именем name на адрес email_address с содержанием text.

1. Реализуйте функцию to_Timur() с помощью функции partial(), которая принимает один аргумент:
    text — содержание письма

Функция должна отправлять письмо пользователю с именем Тимур на адрес timyrik20@beegeek.ru с
содержанием text.

2. Реализуйте функцию send_an_invitation() с помощью функции partial(), которая принимает два
аргумента в следующем порядке:
    name — имя
    email_address — адрес электронной почты

Функция должна отправлять письмо на имя name и на адрес email_address со следующим содержанием:

Школа BEEGEEK приглашает Вас на новый курс по программированию на языке Python.
тут....

Примечание 1. Функции to_Timur() и send_an_invitation() должны являться partial объектами.
"""

from functools import partial


def send_email(name, email_address, text):
    return f'В письме для {name} на адрес {email_address} сказано следующее: {text}'


to_Timur = partial(send_email, 'Тимур', 'timyrik20@beegeek.ru')
send_an_invitation = partial(send_email, text='Школа BEEGEEK приглашает Вас на новый курс по '
                                              'программированию на языке Python. тутут....')

# INPUT DATA:

# TEST_1:
print(to_Timur('когда курс?'))
# В письме для Тимур на адрес timyrik20@beegeek.ru сказано следующее: когда курс?

# TEST_2:
print(to_Timur('Тимур, привет, я на егэ, помоги решить 13 задачу'))

# TEST_3:
print(to_Timur('хочу курс по искусственным интеллектам и криптовалютам бесплатно и завтра'))

# TEST_4:
try:
    to_Timur()
except:
    print('ok')

# TEST_5:
try:
    to_Timur('первое', 'второе')
except:
    print('ok')

# TEST_6:
try:
    to_Timur('первое', 'второе', 'третье')
except:
    print('ok')

# TEST_7:
try:
    to_Timur('beegeek')
    print('ok')
except:
    print('ne ok')

# TEST_8:
print(send_an_invitation("Тимур", "timyrik20@beegeek.ru"))

# TEST_9:
try:
    print(send_an_invitation("Тимур"))
except:
    print("Ошибка, и где же? Хм-м-м")

# TEST_10:
print(to_Timur(
    'Здравствуйте! Я Таня из компании Орифлэйм. Хочу предложить вам новую линейку курсов от '
    'Поколения Python'))

# TEST_11:
print(to_Timur('This is... Requiem. What you are seeing is indeed the truth.'))
