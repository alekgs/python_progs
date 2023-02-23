"""
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
    число a – должно быть палиндромом;
    число b – должно быть простым;
    число c – должно быть четным.
Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое значение
пароля password и возвращает значение True если пароль является действительным паролем BEEGEEK банка
и False в противном случае.
  число a – должно быть палиндромом;
  число b – должно быть простым;
  число c – должно быть четным.
"""


# функция проверки палиндрома
def is_palindrome(text):
    return text == text[::-1]


# функция проверки простых чисел
def is_prime(num):
    num = int(num)
    return len([i for i in range(1, num + 1) if num % i == 0]) == 2


# функция проверки чётности
def is_even(num):
    return int(num) % 2 == 0


def is_valid_password(password):
    lst = password.split(':')
    if len(lst) == 3:
        return is_palindrome(lst[0]) and is_prime(lst[1]) and is_even((lst[2]))
    else:
        return False


# считываем данные
psw = '11111:71:90000'

# вызываем функцию
print(is_valid_password(psw))
