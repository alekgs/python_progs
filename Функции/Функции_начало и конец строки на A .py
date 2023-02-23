"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает строковый аргумент и возвращает
значение True, если переданный аргумент начинается и заканчивается на английскую букву a (регистр буквы неважен) и
False в противном случае.

Примечание 1. Следующий программный код:

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))

должен выводить:

False
False
True
False
False
True
"""
func = lambda x: x[0].lower() == x[-1].lower() == 'a'

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))