"""
Дополните приведенный ниже код, чтобы переменная regex содержала регулярное выражение,
которому соответствуют строки, удовлетворяющие следующим условиям:
    строка начинается с Mr., Mrs., Ms., Dr. или Er.
    оставшаяся часть строки состоит только из одной или более букв латинского алфавита
    в произвольном регистре

Sample Input 1:
Mr.Guev

Sample Output 1:
Mr.Guev

Sample Input 2:
Ms.Jones

Sample Output 2:
Ms.Jones

Sample Input 3:
Dr. Guev

Sample Output 3:

Sample Input 4:
MRS.Traveler

Sample Output 4:

"""

from re import findall

# regex = r'^Mr\.[a-zA-Z]+$|' \
#         r'^Mrs\.[a-zA-Z]+$|' \
#         r'^Ms\.[a-zA-Z]+$|' \
#         r'^Dr\.[a-zA-Z]+$|' \
#         r'^Er\.[a-zA-Z]+$'

regex = '^[MDE]r\.[a-zA-Z]+$|^Mr?s\.[a-zA-Z]+$'

print(*findall(regex, input()))
