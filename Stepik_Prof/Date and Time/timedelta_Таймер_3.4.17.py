"""
Таймер

Часы показывают время в формате HH:MM:SS. На этих часах запустили таймер, который прозвенит через nn секунд. Напишите
программу, которое определит, какое время будет на часах, когда прозвенит таймер.

Формат входных данных
На вход программе в первой строке подается текущее время на часах в формате HH:MM:SS.
В следующей строке вводится целое неотрицательное число n — количество секунд, через которое должен прозвенеть таймер.

Формат выходных данных
Программа должна вывести время в формате HH:MM:SS, которое будет на часах, когда прозвенит таймер.


Sample Input 1:
09:00:00
90

Sample Output 1:
09:01:30

Sample Input 2:
23:59:59
1

Sample Output 2:
00:00:00

Sample Input 3:
13:34:46
456

Sample Output 3:
13:42:22
"""

from datetime import datetime, timedelta
# from time import sleep

mask = '%H:%M:%S'
time_end = datetime.strptime(input(), mask) + timedelta(seconds=int(input()))
print(time_end.strftime(mask))


# t = timedelta(seconds=1)
# while t <= td:
#     print(f'\r{t_now + t}', end='')
#     sleep(1)
#     t += timedelta(seconds=1)
#
# print('Сработал таймер !')
