n = int(input())

first = '* * * *'
second = ' * * * '

if n % 2 == 0:
    for i in range(n // 2):
        print(first + '\n' + second, sep='\n')
else:
    for i in range(n):
        if i % 2:
            print(second)
        else:
            print(first)
