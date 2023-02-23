# Алгоритм нахождения всех делителей целого числа
#
hello = '* Программа для нахождения всех делителей целого числа *'
print('*' * len(hello))
print(hello)
print('*' * len(hello))

n, i, s = int(input('Введите целое число: ')), 1, []
print(f'Делители числа {n}:')
while i * i < n:
    if n % i == 0:
        s.append(i)
        if i != n // i:
            s.append(n // i)
    i += 1
s.sort()
print(*s)
#
