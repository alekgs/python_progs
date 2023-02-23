# какое количество чисел можно составить из 3-х значного числа ?
#
n = int(input())

if 100 <= n <= 999:
    n1 = n // 100
    n2 = n // 10 % 10
    n3 = n % 10

    if not n % 100 or (n1 == n2 == n3):
        print('одно число')
    else:
        if n1 and n2 and n3:
            if n1 == n2 or n2 == n3 or n1 == n3:
                print('три числа')
            else:
                print('шесть чисел')
        if (n1 and n2 and not n3) or (n1 and not n2 and n3):
            print('четыре числа')
else:
    print('ошибка')
