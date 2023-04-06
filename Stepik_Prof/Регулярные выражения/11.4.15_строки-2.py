"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют строки, удовлетворяющие следующим условиям:
    строка содержит исключительно буквы латинского алфавита в произвольном регистре
    строка оканчивается латинской буквой s в нижнем регистре

Sample Input 1:
Chess

Sample Output 1:
Chess

Sample Input 2:
exodus

Sample Output 2:
exodus

Sample Input 3:
Diablo

Sample Output 3:

"""

from re import findall

regex = r'[a-zA-Z]*s$'
print(*findall(regex, input()))
