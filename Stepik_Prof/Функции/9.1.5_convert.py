"""
Функция convert()

Реализуйте функцию convert(), которая принимает один аргумент:
    number — целое число

Функция должна возвращать кортеж из трех элементов, расположенных в следующем порядке:
    двоичное представление числа number в виде строки без префикса 0b
    восьмеричное представление числа number в виде строки без префикса 0o
    шестнадцатеричное представление числа number в виде строки в верхнем регистре без префикса 0x

Примечание 1. В задаче удобно воспользоваться функциями bin(), oct() и hex().

Sample Input 1:
print(convert(15))

Sample Output 1:
('1111', '17', 'F')

Sample Input 2:
print(convert(-24))

Sample Output 2:
('-11000', '-30', '-18')

Sample Input 3:
print(convert(1))

Sample Output 3:
('1', '1', '1')
"""


def convert(number: int) -> tuple:
    return f'{number:b}', f'{number:o}', f'{number:X}'


# convert = lambda n: tuple(f'{n:{f}}' for f in 'boX')

print(convert(15))
print(convert(-24))
print(convert(1))
