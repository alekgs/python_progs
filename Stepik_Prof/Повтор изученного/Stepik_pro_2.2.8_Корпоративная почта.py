"""
Корпоративная почта 🌶️
В онлайн-школе "BEEGEEK" сотрудникам положена корпоративная почта, которая формируется как <имя-фамилия>@beegeek.bzz,
например, timyr-guev@beegeek.bzz. При таком подходе существует проблема тёзок. Для решения такой проблемы было решено
приписывать справа номер. Тогда первый Тимур Гуев получает ящик timyr-guev@beegeek.bzz (без номера),
второй — timyr-guev1@beegeek.bzz, третий — timyr-guev2@beegeek.bzz, и так далее.
Вам дан список уже занятых ящиков в порядке их выдачи и имена-фамилии новых сотрудников в заранее подготовленном виде
(латиницей с символом - между ними). Напишите программу, которая раздает корпоративные ящики новым сотрудникам школы.

Формат входных данных
На вход программе в первой строке подается целое неотрицательное число n — количество выданных
ящиков. В следующих n строках перечислены сами ящики в порядке выдачи, по одному на строке. На следующей строке
задано целое неотрицательное число m — количество новых сотрудников, которым нужно раздать корпоративные ящики.
Каждая из последующих m строк представляет собой имя и фамилию сотрудника в подготовленном к использованию формате.

Формат выходных данных
Программа должна вывести почтовые ящики (m строк) для новых сотрудников в том порядке, в котором они раздавались.

Sample Input 1:
6
ivan-petrov@beegeek.bzz
petr-ivanov@beegeek.bzz
ivan-petrov1@beegeek.bzz
ivan-ivanov@beegeek.bzz
ivan-ivanov1@beegeek.bzz
ivan-ivanov2@beegeek.bzz
3
ivan-ivanov
petr-petrov
petr-ivanov

Sample Output 1:
ivan-ivanov3@beegeek.bzz
petr-petrov@beegeek.bzz
petr-ivanov1@beegeek.bzz

Sample Input 2:
2
timyr-guev2@beegeek.bzz
anri-tabuev@beegeek.bzz
3
timyr-guev
timyr-guev
anri-tabuev

Sample Output 2:
timyr-guev@beegeek.bzz
timyr-guev1@beegeek.bzz
anri-tabuev1@beegeek.bzz
"""
# ######## Решение от Тимура Гуева (немного шлифанул :-) )
#
digits, result_lst, domain = '0123456789', [], '@beegeek.bzz'
# used_lst = [input().split(domain)[0] for _ in range(int(input()))]
used_lst = [input().rstrip(domain) for _ in range(int(input()))]

for _ in range(int(input())):
    name = input()
    count = 1
    while name in used_lst:
        name = name.rstrip(digits) + str(count)
        count += 1
    used_lst.append(name)
    result_lst.append(f'{name}{domain}')

print(*result_lst, sep='\n')
#

# ############### Решение через множества (автор -  Александр Черник)
#
# digits, result_lst, domain = '0123456789', [], '@beegeek.bzz'
# used_lst = set(input().split(domain)[0] for _ in range(int(input())))
# for _ in range(int(input())):
#     name = input()
#     count = 1
#     while name in used_lst:
#         count += 1
#         name = name.rstrip(digits) + str(count)
#     used_lst.add(name)
#     result_lst.append(f'{name}{domain}')
# print(*result_lst, sep='\n')

