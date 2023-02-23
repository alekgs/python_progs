"""
Напишите программу, которая определяет день недели, соответствующий заданной дате.

Формат входных данных
На вход программе подается дата в формате YYYY-MM-DD.

Формат выходных данных
Программа должна вывести полное название дня недели на английском, который соответствует введенной дате.

Примечание. Тестовые данные доступны по ссылке.
Sample Input 1:
2021-12-10

Sample Output 1:
Friday

Sample Input 2:
2022-01-03

Sample Output 2:
Monday

Sample Input 3:
2021-11-02

Sample Output 3:
Tuesday
"""

from datetime import datetime

print(datetime.fromisoformat(input()).strftime('%A'))
