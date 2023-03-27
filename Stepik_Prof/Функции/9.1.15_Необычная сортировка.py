"""
Необычная сортировка 🌶️

Дана строка, содержащая латинские буквы и цифры. Напишите программу, которая сортирует символы в строке согласно
следующим правилам:

    все отсортированные строчные буквы стоят перед заглавными буквами
    все отсортированные заглавные буквы стоят перед цифрами
    все отсортированные нечетные цифры стоят перед отсортированными четными

Формат входных данных
На вход программе подается строка, содержащая латинские буквы и цифры.

Формат выходных данных
Программа должна расположить символы в строке в соответствии с условием задачи и вывести полученный результат.
"""

# lower, upper, even, odd = [], [], [], []
#
# for i in list(input()):
#     if i.islower():
#         lower.append(i)
#     elif i.isupper():
#         upper.append(i)
#     elif i.isdigit():
#         if int(i) % 2:
#             odd.append(i)
#         else:
#             even.append(i)
#
# res = ''
# for s in [lower, upper, odd, even]:
#     res += ''.join(sorted(s))
# print(res)

# print(''.join(sorted(input(), key=lambda x: (x in '24680', x.isdigit(), x.isupper(), x))))


# def comparator(char):
#     if char.isalpha():
#         return 0, char.isupper(), char
#     digit = int(char)
#     return 1, not digit % 2, digit
#
#
# print(''.join(sorted(input(), key=comparator)))


from string import ascii_lowercase, ascii_uppercase

sorted_symbols = ascii_lowercase + ascii_uppercase + '13579' + '02468'
print(''.join(sorted(input(), key=sorted_symbols.index)))

# Sample Input 1:
# Sorting1234

# Sample Output 1:
# ginortS1324

# Sample Input 2:
# n0tEast3rEgg

# Sample Output 2:
# aggnrsttEE30

# Sample Input 3:
# 3DYrz34UXl

# Sample Output 3:
# lrzDUXY334


# AnHTqir9brdQrgu5g71uhm1FaJ4fAZjbisIDnJVYekRPdGDc29
# abbcddefgghiijkmnnqrrrsuuAADDFGHIJJPQRTVYZ11579924
# abbcddefgghiijkmnnqrrrsuuAADDFGHIJJPQRTVYZ11579924