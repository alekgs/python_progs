"""
Вводится строка - квадратное уравнение вида ax2+bx+c=0ax2+bx+c=0 (без пробелов, aa , bb , cc - натуральные числа).
Нужно вывести список коэффициентов уравнения.
Пример
Ввод
14x^2+4x+1024=0
Вывод
['14', '4', '1024']
"""
k = input()[:-2].split('+')
print([s.split('x')[0] for s in k])

