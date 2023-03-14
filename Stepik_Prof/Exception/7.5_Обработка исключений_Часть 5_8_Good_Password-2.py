"""
Функция is_good_password() 🐍

Назовем пароль хорошим, если
    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле EAFP, которая принимает один аргумент:
    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или возбуждать исключение:
    LengthError, если его длина меньше 99 символов
    LetterError, если в нем отсутствуют буквы или все буквы имеют одинаковый регистр
    DigitError, если в нем нет ни одной цифры

Примечание 1.
Исключения LengthError, LetterError и DigitError уже определены и доступны.

Примечание 2.
Приоритет возбуждения исключений в случае невыполнения нескольких условий:
LengthError, затем LetterError, а уже после DigitError.


"""


class PasswordError(Exception):
    ...


class LengthError(PasswordError):
    ...


class LetterError(PasswordError):
    ...


class DigitError(PasswordError):
    ...


def is_good_password(passw: str) -> bool:
    if len(passw) < 9:
        raise LengthError
    if passw.upper() == passw or passw.lower() == passw:
        raise LetterError
    if not any((True for char in passw if char.isdigit())):
        raise DigitError
    return True


# INPUT DATA:

# TEST_1:
try:
    print(is_good_password('As1234567890'))
except Exception as err:
    print(type(err))

# TEST_2:
print(is_good_password('еПQSНгиfУЙ70qE'))

# TEST_3:
try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(err)

# TEST_4:
try:
    print(is_good_password('МойПарольСамыйЛучший111'))
except Exception as err:
    print(type(err))

# TEST_5:
try:
    print(is_good_password('4abcdABC'))
except Exception as err:
    print(type(err))

# TEST_6:
try:
    print(is_good_password('4abcdABC8'))
except Exception as err:
    print(type(err))

# TEST_7:
try:
    print(is_good_password('abc!@#%$#%#$%^&dABC8'))
except Exception as err:
    print(type(err))

# TEST_8:
try:
    print(is_good_password('!@#$%^&*()_+'))
except Exception as err:
    print(type(err))

# TEST_9:
try:
    print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))
except Exception as err:
    print(type(err))

# TEST_10:
try:
    print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
except Exception as err:
    print(type(err))

# TEST_11:
try:
    print(is_good_password('qwertyтимур696969'))
except Exception as err:
    print(type(err))

# TEST_12:
try:
    print(is_good_password('1234567890'))
except Exception as err:
    print(type(err))

# TEST_13:
try:
    print(is_good_password('123456789A'))
except Exception as err:
    print(type(err))

# TEST_14:
try:
    print(is_good_password('123456789a'))
except Exception as err:
    print(type(err))