"""
Каждому гражданину страны Утопия выдается идентификационный номер, который имеет следующий формат:

    номер начинается с 0—3 строчных латинских букв включительно
    далее следует последовательность цифр, длина которой должна быть от 2 до 8 включительно
    после цифр указываются 3 или более заглавные латинские буквы

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому
соответствуют идентификационные номера граждан Утопии.

Sample Input 1:
Dear citizen! Your old ID: tba44891AHH, your new ID: 781AHHGYT

Sample Output 1:
tba44891AHH 781AHHGYT

Sample Input 2:
1. name Tobot id: 234AZXR, 2. name Alph id: a6578ALPH, 3. name Teta id: abra0909CADABRA 4. name Alph up id: A6578ALPH

Sample Output 2:
234AZXR a6578ALPH bra0909CADABRA 6578ALPH
"""

from re import findall

regex = r'[a-z]{,3}\d{2,8}[A-Z]{3,}'

print(*findall(regex, input()))
