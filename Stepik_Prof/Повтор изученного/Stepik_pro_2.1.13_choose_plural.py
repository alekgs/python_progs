"""
Функция choose_plural()

Реализуйте функцию choose_plural(), которая принимает два аргумента в следующем порядке:
    amount — натуральное число, количество
    declensions — кортеж из трех вариантов склонения существительного

Функция должна возвращать строку, полученную путем объединения подходящего существительного
из кортежа declensions и количества amount, в следующем формате:

<количество> <существительное>

Примечание.
Передаваемый в функцию кортеж легко составить по мнемоническому правилу: один, два, пять.

Например:
    для слова «арбуз»: арбуз, арбуза, арбузов
    для слова «рубль»: рубль, рубля, рублей


Sample Input 1:
print(choose_plural(21, ('пример', 'примера', 'примеров')))

Sample Output 1:
21 пример

Sample Input 2:
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

Sample Output 2:
92 гвоздя

Sample Input 3:
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))

Sample Output 3:
8 яблок

"""
#
#
# def choose_plural(amount: int, declensions: tuple):
#     w = declensions[1]
#     if str(amount).endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
#         w = declensions[2]
#     elif str(amount).endswith('1'):
#         w = declensions[0]
#     return f'{amount} {w}'


def choose_plural(amount: int, declensions: tuple) -> str:
    """
    Возвращает строку, полученную путем объединения подходящего существительного
    из кортежа declensions и количества amount
    """
    d = {
         1: declensions[0],
         2: declensions[1],
         3: declensions[1],
         4: declensions[1],
         5: declensions[2],
         6: declensions[2],
         7: declensions[2],
         8: declensions[2],
         9: declensions[2],
         0: declensions[2]
         }

    return f'{amount} {(d[amount % 10], declensions[2])[10 < amount % 100 < 20]}'


# тесты
print(choose_plural(21, ('пример', 'примера', 'примеров')))  # 21 пример
print(choose_plural(12, ('гвоздь', 'гвоздя', 'гвоздей')))  # 92 гвоздя
print(choose_plural(30, ('яблоко', 'яблока', 'яблок')))  # 8 яблок
print(choose_plural(111223, ('копейка', 'копейки', 'копеек')))
print(choose_plural(763434, ('рубль', 'рубля', 'рублей')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))
print(choose_plural(59, ('помидор', 'помидора', 'помидоров')))
print(choose_plural(240, ('курица', 'курицы', 'куриц')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(12, ('стул', 'стула', 'стульев')))
print(choose_plural(13, ('стул', 'стула', 'стульев')))
print(choose_plural(20, ('стул', 'стула', 'стульев')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))
print(choose_plural(2, ('пример', 'примера', 'примеров')))
print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))
