"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют почтовые индексы Великобритании, удовлетворяющие следующим условиям:
почтовый индекс начинается с одной или двух заглавных латинских букв, за которыми следует одна
цифра. После цифры может следовать один необязательный символ — цифра или заглавная латинская
буква далее через пробел указываются одна цифра и любые две заглавные латинские буквы,
кроме C, I, K, M, O, V

Sample Input 1:
Our postcodes. Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS

Sample Output 1:
NW11 8AB P01 3AX N16 6PS

Sample Input 2:
my postcode is: 1 1PR, but it's not correct, my another postcode P0Z 9AU, it's correct, Artur's postcode CI0 0GG, it's correct, Timur's postcode CIK7O 8JH, it's not correct

Sample Output 2:
P0Z 9AU CI0 0GG IK7O 8JH

# TEST_3:
# Mixed postcodes: PX01 0__, a0A0A 9Aa90, FNceie00dmIJ3 3nxijnd0 DB 90,
#

# TEST_4:
PXA 0AB, PX_A 0AB PY0T 0HN OP111 1LP
# PY0T 0HN

# TEST_5:
PR0V 3RUA6. 0GHZ9a 9UY
# PR0V 3RU

# TEST_6:
PR0V3RKPY0T 0HNP0Z9AU CI00GGIK7O 8JH
# PY0T 0HN IK7O 8JH

# TEST_7:
PR1V ET, oops PR1V 0ET CO0L _PRO
# PR1V 0ET

# TEST_8:
PY0T 0H- IK7O 8J_ PR1V 0Et IJ3 3nX KA1K 1\% tak nado TI1M 1UY
# TI1M 1UY

# TEST_9:
PR1V 0EC TI1M 1IY TI1M 1KO PR1М 0Е PR1V 0MV
#


# TEST_3:
# Mixed postcodes: PX01 0__, a0A0A 9Aa90, FNceie00dmIJ3 3nxijnd0 DB 90,
#

# TEST_8:
PY0T 0H- IK7O 8J_ PR1V 0Et IJ3 3nX KA1K 1\% tak nado TI1M 1UY
# TI1M 1UY
"""

from re import findall

# regex = r'[A-Z]{1,2}\d[\dA-Z]?\s\d[^a-z\d\WCIKMOV]{2}'
regex = r'[A-Z]{1,2}\d[\dA-Z]?\s\d[ABD-HJLNP-UW-Z]{2}'
print(*findall(regex, input()))
