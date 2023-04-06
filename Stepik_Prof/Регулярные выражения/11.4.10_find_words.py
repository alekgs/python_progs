"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют слова a, A, an и An.

Примечание 1.
Словом будем считать последовательность символов, соответствующих \w,
окруженную символами, соответствующими \W


Sample Input 1:
A cow is an animal.

Sample Output 1:
A an

Sample Input 2:
I have been reading this text for aN hour. Сan you give me this book? AN or an apple

Sample Output 2:
an

Sample Input 3:
An acle, a Ancle, A antarktida, an Any

Sample Output 3:
An a A an
"""

from re import findall

regex = r'\b[Aa]n?\b'
print(*findall(regex, input()))
