"""

"""
file = open('111.txt', 'a+', encoding='utf-8')
# извлекаем построчно в цикле
# for row in file:
#     print(row)
# список из строк
# s = file.readlines()
s = file.read().splitlines()
# s = list(map(str.strip, file.readlines()))
print(s)
file.close()
