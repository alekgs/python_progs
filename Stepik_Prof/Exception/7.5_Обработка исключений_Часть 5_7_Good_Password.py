"""
Функция is_good_password() 👀

Назовем пароль хорошим, если
    его длина равна 9 или более символам
    в нем присутствуют большие и маленькие буквы любого алфавита
    в нем имеется хотя бы одна цифра

Реализуйте функцию is_good_password() в стиле LBYL, которая принимает один аргумент:
    string — произвольная строка

Функция должна возвращать True, если строка string представляет собой хороший пароль, или False в противном случае.

"""

from time import perf_counter
# from re import search
#
# def is_good_password(arg):
#     regex = r"^(?=.*\d)(?=.*[а-яa-z])(?=.*[А-ЯA-Z])[\D\d]{9,}$"
#     return bool(search(regex, arg))


def is_good_password(p):
    return len(p) > 8 and p.upper() != p and p.lower() != p and any(i.isdigit() for i in p)


# def is_good_password(passw: str) -> bool:
#     """
#     Функция должна возвращать True, если строка string представляет собой хороший пароль,
#     или False в противном случае
#     :param passw: строка с паролем для проверки
#     :return: результат проверки (True or False)
#     """
#
#     if len(passw) < 9:
#         return False
#
#     is_upper, is_lower, is_digit = False, False, False
#     for char in passw:
#         if char.isupper():
#             is_upper = True
#         elif char.islower():
#             is_lower = True
#         elif char.isdigit():
#             is_digit = True
#
#     return all((is_upper, is_lower, is_digit))

start = perf_counter()
# INPUT DATA:

# TEST_1:
print(is_good_password('41157082'))
#
# False

# TEST_2:
print(is_good_password('мойпарольсамыйлучший'))
# False

# TEST_3:
print(is_good_password('МойПарольСамыйЛучший111'))
# True

# TEST_4:
print(is_good_password('4abcdABC'))
# False

# TEST_5:
print(is_good_password('4abcdABC8'))
# True

# TEST_6:
print(is_good_password('abc!@#%$#%#$%^&dABC8'))
# True

# TEST_7:
print(is_good_password('!@#$%^&*()_+'))
# False

# TEST_8:
print(is_good_password('abc12345678ansdfjkasdkjfbsdk'))
# False

# TEST_9:
print(is_good_password('sjkdfsjkdfhjksdfhjkSDFSDAFSADFSADfsdajf'))
# False

# TEST_10:
print(is_good_password('qwertyтимур696969'))
# False

# TEST_11:
print(is_good_password('1234567890'))
# False
print(perf_counter() - start)
