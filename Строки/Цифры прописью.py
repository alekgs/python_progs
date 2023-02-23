from numtostr_rus import convert as conv

rub, kop = map(int, input('Введите число: ').split('.'))
print(f'{conv(rub)} руб. {conv(kop)} коп.')
