"""
Напишите программу, которая принимает на вход время и выводит целое количество секунд, прошедшее с начала суток.

Формат входных данных
На вход программе подается время в формате HH:MM:SS.

Формат выходных данных
Программа должна вывести целое количество секунд, прошедшее с начала суток.

Примечание 1. Началом суток считается момент времени, соответствующий 00:00:00.

Sample Input 1:
00:01:01

Sample Output 1:
61

Sample Input 2:
00:00:00

Sample Output 2:
0

Sample Input 3:
12:12:12

Sample Output 3:
43932

"""

from datetime import timedelta

h, m, s = map(int, input().split(':'))
td = timedelta(hours=h, minutes=m, seconds=s)
print(td.seconds)

# без timedelta
# from datetime import time
# t = time.fromisoformat(input())
# seconds = t.hour * 3600 + t.minute * 60 + t.second
# print(seconds)
