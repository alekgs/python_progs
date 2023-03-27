"""
Функция verification()

Реализуйте функцию verification(), которая проверяет правильность введенного пароля. Она должна принимать четыре
аргумента в следующем порядке:

    login — логин пользователя
    password — пароль пользователя
    success — некоторая функция
    failure — некоторая функция

Пароль считается правильным, если в нем присутствует, хотя бы одна заглавная латинская буква, хотя бы одна строчная
латинская буква и хотя бы одна цифра. Функция verification() должна вызывать функцию success() с аргументом login,
если переданный пароль является правильным, иначе — функцию failure() с аргументами login и строкой-сообщением об
ошибке:

    в пароле нет ни одной буквы, если в пароле отсутствуют латинские буквы
    в пароле нет ни одной заглавной буквы, если в пароле отсутствуют заглавные латинские буквы
    в пароле нет ни одной строчной буквы, если в пароле отсутствуют строчные латинские буквы
    в пароле нет ни одной цифры, если в пароле отсутствуют цифры

Примечание 1. Если пароль не удовлетворяет нескольким условиям, то приоритеты выбора строки-сообщения об ошибке
являются следующими:

    в пароле нет ни одной буквы
    в пароле нет ни одной заглавной буквы
    в пароле нет ни одной строчной буквы
    в пароле нет ни одной цифры
"""

# def verification(login, password, success, failure):
#     vd = {(str.isalpha, str.isascii): 'в пароле нет ни одной буквы',
#           (str.isascii, str.islower): 'в пароле нет ни одной строчной буквы',
#           (str.isascii, str.isupper): 'в пароле нет ни одной заглавной буквы',
#           (bool,        str.isdigit): 'в пароле нет ни одной цифры'}
#     for f in vd:
#         if not any(f[0](i) and f[1](i) for i in password):
#             return failure(login, vd[f])
#     success(login)

# from string import ascii_letters as let, digits as dig
#
#
# def verification(login, password, success, failure):
#     password = ''.join(set(password) & set(let + dig))
#     if not any(map(lambda x: True if x in let else False, password)):
#         failure(login, 'в пароле нет ни одной буквы')
#     elif password.lower() == password:
#         failure(login, 'в пароле нет ни одной заглавной буквы')
#     elif password.upper() == password:
#         failure(login, 'в пароле нет ни одной строчной буквы')
#     elif not any(filter(lambda x: True if x in dig else False, password)):
#         failure(login, 'в пароле нет ни одной цифры')
#     else:
#         success(login)

# from string import ascii_letters, ascii_uppercase, ascii_lowercase, digits
#
#
# def verification(login, password, success, failure):
#     if not any(map(lambda x: x in ascii_letters, password)):
#         failure(login, 'в пароле нет ни одной буквы')
#     elif not any(map(lambda x: x in ascii_uppercase, password)):
#         failure(login, 'в пароле нет ни одной заглавной буквы')
#     elif not any(map(lambda x: x in ascii_lowercase, password)):
#         failure(login, 'в пароле нет ни одной строчной буквы')
#     elif not any(map(lambda x: x in digits, password)):
#         failure(login, 'в пароле нет ни одной цифры')
#     else:
#         success(login)


# from string import digits as dig, ascii_letters as let
#
#
# def verification(login, pas, success, failure):
#     verif = set(pas) & (set(dig) | set(let))
#
#     responce = {'isalpha': 'в пароле нет ни одной буквы',
#                 'islower': 'в пароле нет ни одной строчной буквы',
#                 'isupper': 'в пароле нет ни одной заглавной буквы',
#                 'isdigit': 'в пароле нет ни одной цифры'}
#
#     for move in responce:
#         if not eval(f'any(i.{move}() for i in verif)'):
#             return failure(login, responce[move])
#
#     return success(login)


from string import ascii_letters, ascii_lowercase, ascii_uppercase


def verification(login, password, success, failure):
    try:
        assert set(password) & set(ascii_letters), 'в пароле нет ни одной буквы'
        assert set(password) & set(ascii_uppercase), 'в пароле нет ни одной заглавной буквы'
        assert set(password) & set(ascii_lowercase), 'в пароле нет ни одной строчной буквы'
        assert set(password) & set('0123456789'), 'в пароле нет ни одной цифры'
    except AssertionError as e:
        failure(login, e)
    else:
        success(login)

# import re
#
# def verification(login, password, success, failure):
#     d = {
#         r'[a-zA-Z]': 'в пароле нет ни одной буквы',
#         r'[A-Z]': 'в пароле нет ни одной заглавной буквы',
#         r'[a-z]': 'в пароле нет ни одной строчной буквы',
#         r'[0-9]': 'в пароле нет ни одной цифры'
#         }
#
#     for k, v in d.items():
#         if not re.search(k, password):
#             return failure(login, v)
#
#     return success(login)


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


# INPUT DATA:

# TEST_1:
def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')


verification('timyrik20', 'Beegeek314', success, failure)


# TEST_2:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)


# TEST_3:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'HELLO_WORLD', success, failure)


# TEST_4:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', '797777777777', success, failure)


# TEST_5:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'Python777', success, failure)


# TEST_6:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'qwerty', success, failure)


# TEST_7:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)


# TEST_8:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольbee123', success, failure)


# TEST_9:
def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпарольBEE123', success, failure)
