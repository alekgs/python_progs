"""
Функция polynom()

Реализуйте функцию polynom(), которая принимает один аргумент:
    x — вещественное число

Функция должна возвращать значение выражения x2+1x2+1.

Также функция должна иметь атрибут values, представляющий собой множество (тип set) всех значений
функции, которые уже были вычислены.


Sample Input 1:
print(polynom(5))
print(polynom.values)

Sample Output 1:
26
{26}

Sample Input 2:
polynom(1)
polynom(2)
polynom(3)
print(*sorted(polynom.values))

Sample Output 2:
2 5 10

Sample Input 3:
for _ in range(10):
    polynom(10)

print(polynom.values)

Sample Output 3:


Имеется словарь polynom.__dict__, в этом словаре нужно создать ключ 'values' со значением -
пустое множество. Далее в это множество добавляем  x ** 2 + 1. И возвращаем то, что просят по
условию

"""


def polynom(x):
    polynom.__dict__.setdefault('values', set())
    res = x ** 2 + 1
    polynom.values.add(res)
    return res


print(polynom(5))
print(polynom.values)

polynom(1)
polynom(2)
polynom(3)
print(*sorted(polynom.values))

[polynom(10) for _ in range(10)]
print(polynom.values)
