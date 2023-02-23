from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation =  '!#$%&*+-=?@^_.'
chars = ''


def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += choice(chars)
    return print(password)


n = int(input('Количество паролей для генерации: '))
len_psw = int(input('Длина одного пароля: '))
nums = input('Включать ли цифры 0123456789 ? (y/n) : ')
up_letters = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ ? (y/n): ')
lo_letters = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz ? (y/n): ')
symbols = input('Включать ли символы !#$%&*+-=?@^_? (y/n): ')
n_symbols = input('Исключать ли неоднозначные символы il1Lo0O ? (y/n): ')

if nums.lower() == 'y':
    chars += digits
if up_letters.lower() == 'y':
    chars += uppercase_letters
if lo_letters.lower() == 'y':
    chars += lowercase_letters
if symbols.lower() == 'y':
    chars += punctuation
if n_symbols.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')


for _ in range(n):
    generate_password(len_psw, chars)

