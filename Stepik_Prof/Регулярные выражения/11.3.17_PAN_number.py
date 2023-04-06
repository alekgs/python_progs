"""
PAN (Permanent Account Number) – это уникальный номер, который присваивается всем
налогоплательщикам в Индии. Он имеет следующий формат:

<letter><letter><letter><letter><letter><digit><digit><digit><digit><letter>

PAN всегда состоит из 10 символов, в котором letter
— заглавная латинская буква, а digit — цифра.

Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение, которому
соответствуют PAN номера.

Sample Input 1:
The PAN (or PAN number) is a ten-character long alpha-numeric unique identifier. Example: AAAPZ1234C

Sample Output 1:
AAAPZ1234C

Sample Input 2:
first number is ABCD EZZPA1234ZaPMQ0000O, check thusEZZPA1234ZAPMQ0000O,

Sample Output 2:
EZZPA1234Z EZZPA1234Z
"""

import re

regex = r'[A-Z]{5}\d{4}[A-Z]'

print(*re.findall(regex, input()))
