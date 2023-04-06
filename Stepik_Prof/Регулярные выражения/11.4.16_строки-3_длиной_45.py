"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют строки длины 45, удовлетворяющие следующим условиям:

первые 40 символов являются либо латинскими буквами произвольного регистра, либо четными цифрами
последние 5 символов являются либо нечетными цифрами, либо символами пробела

Sample Input 1:
BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111

Sample Output 1:
BpOBNpqKg4EgPKxWn8wavcQMOP06nbCwvOdu6CPj11111

Sample Input 2:
BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791

Sample Output 2:
BTJubHCvbwTQEN2BqQJsgAIDW4bcyFyUp4COdUO4 3791

Sample Input 3:
Sufk6dm7ECNGRlJ7VsIB7HvBOvSgAoN9gIUOqwy4

Sample Output 3:

"""

from re import findall

regex = r'^[a-zA-Z02468]{40}[13579\s]{5}$'
print(*findall(regex, input()))
