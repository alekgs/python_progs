"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют слова, начинающиеся с латинской заглавной буквы.

Sample Input 1:
I signed up in the app using my Apple ID. How can I sign in to the web version?

Sample Output 1:
I Apple ID How I

Sample Input 2:
I can Do it MYSELF

Sample Output 2:
I Do MYSELF

Sample Input 3:
How are --U--

Sample Output 3:
How U
"""

from re import findall

regex = r'\b[A-Z]\w*\b'
print(*findall(regex, input()))
