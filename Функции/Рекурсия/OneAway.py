# Ровно в одном
#
# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова word1 и word2
# и возвращает значение True если слова имеют одинаковую длину и отличаются ровно в 1 символе и False
# в противном случае.
#
#  Примечание. Следующий программный код:
#
# print(is_one_away('bike', 'hike'))
# print(is_one_away('water', 'wafer'))
# print(is_one_away('abcd', 'abpo'))
# print(is_one_away('abcd', 'abcde'))
#
# должен выводить:
#
# True
# True
# False
# False


def is_one_away(word1, word2):

    if len(word1) != len(word2):
        return False

    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    return True if count == 1 else False


# считываем данные
# txt1 = input()
# txt2 = input()

txt1 = 'cff'
txt2 = 'cfe'


# вызываем функцию
print(is_one_away(txt1, txt2))

s = 'Hello world!\n'
print(s * 5)


