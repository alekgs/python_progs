"""
HTML-элементы — основа языка HTML. Каждый парный HTML-элемент обозначается начальным (
открывающим) и конечным (закрывающим) тегами. Открывающий и закрывающий теги содержат имя
элемента. Комментарии в страницах HTML помещаются между тегами <!-- и -->.

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому
соответствуют комментарии HTML.

Sample Input 1:
Hi, your tags <!-bee-> and <--geek--> are incorrect. Correct tags look like <!--beegeek-->

Sample Output 1:
<!--beegeek-->

Sample Input 2:
<!-- header of page --> <-- incorrect header of page !-->

Sample Output 2:
<!-- header of page -->
"""

import re

regex = r'<!--.*?-->'

print(*re.findall(regex, input()))
