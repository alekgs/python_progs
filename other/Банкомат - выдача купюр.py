"""
У Олега в банке есть n рублей. Он хочет снять всю сумму наличными.
Номиналы купюр равны 100, 200, 500, 1000, 2000, 5000.
Какое минимальное число купюр должен получить Олег после того, как снимет все деньги?
На вход программе поступает одно положительные целое число n.
"""
from time import sleep

print('Добро пожаловать в наш СуперМегаБанк!')
# print('Доступные номиналы купюры для выдачи - 5000, 2000, 1000, 500, 200, 100 руб.')
n, s, lst = int(input('Введите сумму, кратную 5000, 2000, 1000, 500, 200, 100 руб.: ')), \
            0, [5000, 2000, 1000, 500, 200, 100]
kup = []
print('Подсчет наличия... Секундочку ')
sleep(0.5)
print('Получите Ваши денюжки )) ')
print('------------------------')
for i in lst:
    s += n // i
    if n // i != 0:
        kup.append(str(n // i) + ' - ' + str(i) + ' руб.')
    n %= i
print('Всего купюр - ', s)
print(*(i for i in kup), sep='\n')
print('------------------------')
print('Спасибо, приходите к нам ещё.')
print('До свидания !')
