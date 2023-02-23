# Вариант 1
# def is_password_good(password):
#     len_pass = len(password)
#     if len_pass < 8 or not password.isalnum():
#         #       return 'Пароль должен быть > 8 символов !'
#         return False
#     else:
#         up = [i for i in password if i.isupper()]
#         low = [i for i in password if i.islower()]
#         dig = [i for i in password if i.isdigit()]
#
#         #        return 'Ок, пароль надёжный.' if up and low and dig else 'Пароль ненадёжный !'
#         return True if up and low and dig else False
#
#
# # считываем данные
# txt = 'awqeA12345'
#
# # вызываем функцию
# print(is_password_good(txt))


# Вариант 2 (оптимизированный !)
def is_password_good(password):
    if len(password) < 8 or not password.isalnum():
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for c in password:
        if c.isupper():
            flag1 = True
        elif c.islower():
            flag2 = True
        elif c.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3


# считываем данные
txt = 'abcABC12345!'

# вызываем функцию
print(is_password_good(txt))
