"""
Напишите функцию func, используя синтаксис анонимных функций, которая принимает целочисленный аргумент и
возвращает значение True, если он делится без остатка на 19 или на 13 и False в противном случае.

Примечание 1.

Следующий программный код:
print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))

должен выводить:
True
True
False
False
True
"""
func = lambda x: not x % 19 or not x % 13

print(func(19))
print(func(13))
print(func(20))
print(func(15))
print(func(247))
