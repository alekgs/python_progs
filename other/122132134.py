# a, b, c = int(input()), int(input()), int(input())
# if c < a:
#     a, c = c, a
# if b < a:
#     a, b = b, a
# if c < b:
#     b, c = c, b
# print(b)

# a = int(input())
# print('Легкий вес'*(a<60), 'Первый полусредний вес'*(60<=a<64), 'Полусредний вес'*(64<=a<69))

# str1 = '1'
# str2 = str1 + '2' + str1
# str3 = str2 + '3' + str2
# str4 = str3 + '4' + str3
# print(str4)

# print('YES' if 'синий' in input() else 'NO')

# s = input()
# print("YES" if "суббота" in s or "воскресенье" in s else "NO")

# проверка email
# s = input()
# print("YES" if "@" in s and "." in s else "NO")

# m, n = int(input()), int(input())
#
# if m < n:
#      r = range((m, n + 1)
# #    for i in range(m, n + 1):
# #        print (i)
# elif m > n:
#      r = range((m, n - 1)
#  #   for i in range(m, n - 1, -1):
#  #       print (i)
# else:
#     print(m)

# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# num = int(input())
# sum_5 = 0
# while num <= 5 and num >=0:
#     if num == 5:
#         sum_5 += 1
#     num = int(input())
# print(sum_5)

# num = 12345
# while num:
#     i = num % 10
#     num = num // 10
#     print(i)

# mult = 1
# for i in range(1, 11):
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)

# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             print(hours, ':', minutes, ':', seconds)

# from time import *
# for minutes in range(60):
#     for seconds in range(60):
#         print(minutes, ':', seconds, end='')
#         sleep(1)
#         print(end='\r')

# for i in range(1, 4):
#     for j in range(3, 5):
#         print(i + j, end='')
# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 sum = a ** 5 + b ** 5 + c ** 5 + d ** 5
#                 e = int(sum ** (1/5))
#                 if sum == e ** 5:
#                     print(a, b, c, d, e)
#                     print(a + b + c + d + e)
#                     break

# сумма четных чисел в числе
# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# числа Рамануджана
# n = int(input('Введите ограничение диапазона для нахождения чисел Рамануджана: '))
# total = 0
# for n in range(1, n):
#     for k in range(1, n):
#         for m in range(1, n):
#           for t in range(1, n):
#               if n ** 3 + k ** 3 == m ** 3 + t ** 3 and n != t and k != m and k != t and n > k and m > t and n > m:
#                 n, k == m, t
#                 total += 1
#                 print('n =', n, 'k =', k, 'm =', m, 't=', t, '=', n ** 3 + k ** 3)
# print('Общее количество натуральных решений =', total)
#
# s = input('Введите строку: ')
# for i in range(len(s)):
#     print(s[i])
# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')


# # Шифр Цезаря - расшифровка (англ.)
#
# n = int(input('Введите ключ: '))    # Шаг для дешифровки
# s = input('Зашифрованная строка: ') # Текс для дешифровки
# abc = 26                            # Кол-во букв в англиийском алфавите
#
# for i in range(len(s)):         # Делаем цикл в длину текста
#      word = ord(s[i]) - n        # Получаем код из таблице Unicode со смешением
#      if word < 97:               # Если номер вышел за нижнюю границу строчных латинских букв
#          word += abc             # Возвращаем его в границы строчных латинских букв
#      print(chr(word), end='')    # Выводим букву, соответствующюю искомому номеру

# Шифр Цезаря - шифровка
# Текст, который пользователь хочет ввести
# text = input("Введите текст, который хотите зашифровавать: ")
# # Пользователь вводит ключ
# k = int(input("Укажите ключ: "))
# # Пользователь вводит язык текста, который будет зашифрован
# language = input("На каком языке текст, который вы ввели (русский, английский): ")
#
#
# # Функция шифрования с тремя параметрами: текст, ключ, язык
# def ceaser_cipher(user, key, lang):
#     # Переменная результата шифрования; переменная, определяющая верхний и нижний регистр
#     res, n = [], ""
#
#     # Проверка пользователем выбранного языка
#
#     # Проверка выбран ли русский язык (регистр букв, вводимых пользователем, не важен)
#     if lang.lower() in ["русский", "russian"]:
#         # Двум переменным присваиваются русская азбука нижнего и верхнего регистра соответственно
#         dictionary, dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
#     # Проверка выбран ли английский язык язык (регистр букв, вводимых пользователем, не важен)
#     elif lang.lower() in ["английский", "english"]:
#         # Двум переменным присваиваются английской азбука нижнего и верхнего регистра соответственно
#         dictionary, dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     else:
#         return "Такого языка нет в опции"
#
#     # Цикл проверки, где каждую итерацию будет обрабатываться один символ из текста последовательно
#     for i in range(len(user)):
#         # Проверка символа на верхний или нижний регистр
#
#         # Принадлежит ли символ нижнему регистру
#         if user[i] in dictionary:
#             n = dictionary
#         # Принадлежит ли символ верхнему регистру
#         elif user[i] in dictionary_upper:
#             n = dictionary_upper
#         # Символ не принадлежит ни нижнему ни верхнему регистру (символ не является буквой)
#         else:
#             res.append(user[i])
#
#         # Если символ есть в списке n (является буквой), то будет происходить его зашифровка
#         if user[i] in n:
#             # Цикл перебора азбуки
#             for j in range(len(n)):
#                 # Если порядковый номер буквы + ключ находятся  в диапазоне от 0 до конца азбуки
#                 # и если буква из текста совпадает с буквой из азбуки, то:
#                 if 0 <= j + key < len(n) and user[i] == n[j]:
#                     # В результат добавляется буква со сдвигом key (зашифрованная буква)
#                     res.append(n[j + key])
#                 # Если порядковый номер буквы + ключ выходит из диапазона азбуки, превышая его
#                 # и если буква из текста совпадает с буквой из азбуки, то:
#                 elif j + key >= len(n) and user[i] == n[j]:
#                     # В результат добавляеться буква со сдвигом key,
#                     # при этом преводя порядковый номер буквы к диапазону азбуки (зашифрованая буква)
#                     res.append(n[(1 - j - key) % (len(n) - 1)])
#                 # Если порядковый номер буквы + ключ выходит из диапазона азбуки, недотягивает до него
#                 # и если буква из текста совпадает с буквой из азбуки, то:
#                 elif j + key < 0 and user[i] == n[j]:
#                     # В результат добавляется буква со сдвигом key,
#                     # при этом приводя порядковый номер буквы к диапазону азбуки (зашифрованная буква)
#                     res.append(n[(j + key) % len(n)])
#
#     # Функция возвращает зашифрованный текст
#     return ''.join(res)
#
#
# # Вывод зашифрованного текста
# print(ceaser_cipher(text, k, language))

# s = 'карандаш'
# # for i in range(len(s)):
# #     if i % 3 != 0:
# #         print(s[i], end='')
# print(s[1::2])


import time

start_time = time.time()

# for t in range(1000):
#     s = 'h123456789h'
#     h1 = s.find('h') + 1
#     h2 = s.rfind('h')
# print(s[:h1] + s[h2:h1:-1] + s[h2:])

# n = int(input())
# s = ''
# for i in range(n):
#     s += chr(97 + i)
# print(list(s))
# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# rainbow[rainbow.index('Green')] = 'Зеленый'
# rainbow[rainbow.index('Violet')] = 'Фиолетовый'

# numbers1 = [1, 2, 3]
# numbers2 = [6]
# numbers3 = [7, 8, 9, 10, 11, 12, 13]
#
# print(numbers1 * 2 + numbers2 * 9 + numbers3)

# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12,
#            0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# print('YES' if (5 in numbers and 17 in numbers) else 'NO')
# del(numbers[0])
# del(numbers[-1])
# print(numbers)
# l = []
# for i in range(ord('z') - ord('a') + 1):
#     l.append(chr(ord('a') + i) * (i + 1))
# print(l)
# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# s = 0
# for i in numbers:
#     s += i ** 2
# print(s)
# s = '1 2 3 4 5 6 7 8 9 0'
# words = s.split()
#
# print(*words, sep='\n')

# s = 'BEEGEEK'
# chars = list(s)
# s = '**'.join(chars)
# print(s)

# colors = ['Red', 'Blue', 'Green', 'Black', 'White']
# del colors[-1]
# colors.remove('Green')
# print(colors)

# numbers = [8, 9, 10, 11]
# numbers += [4,5,6]
# del numbers[0]
# numbers *= 2
# numbers.insert(3, 25)
# print(numbers)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del',
#             'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#             'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']
#
# new_keywords = [s for s in keywords if len(s) >= 5]
# print(new_keywords)


def is_password_good(password):
    len_pass = len(password)
    if len_pass < 8:
        return 'Пароль должен быть > 8 символов !'
    elif password.isalnum() is False:
        return 'Пароль должен содержать только буквы и цифры !'
    else:
        flag_digit = 0
        flag_alpha_lower = 0
        flag_alpha_upper = 0

        for i in range(len_pass):
            if password[i].isdigit():
                flag_digit += 1
            elif password[i].islower():
                flag_alpha_lower += 1
            elif password[i].isupper():
                flag_alpha_upper += 1

        print(flag_alpha_lower, flag_digit, flag_alpha_upper)
        if flag_alpha_lower != 0 and flag_digit != 0 and flag_alpha_upper != 0:
            return 'Ок, пароль надёжный.'
        else:
            return 'Пароль ненадёжный !'


# считываем данные
txt = 'abc12345XYZ'

# вызываем функцию
print(is_password_good(txt))

print("--- %s seconds ---" % (time.time() - start_time))
