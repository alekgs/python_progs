"""
Требуется написать функцию 'telephonе', которая проверяет правильность ввода номер телефона.
Правильный номер телефона начинается с "+7" и содержит 10 цифр (не считая "+7")

Функция должна вывести (не вернуть!) 'True', в случае, если он правильный, или 'False', если нет.
Пример
Ввод
+749545678

Вывод
False

Примечания
Нужно написать только функцию. Вызов функции писать не нужно!
Функция должна обязательно называться telephone.
"""


def telephonе(num):
    if num[:2] == '+7' and len(num[2:]) == 10 and num[2:].isdigit():
        print(True)
    else:
        print(False)


telephonе('+7913999096z')