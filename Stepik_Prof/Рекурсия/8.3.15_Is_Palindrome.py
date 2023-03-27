"""
Функция is_palindrome()

Реализуйте функцию is_palindrome() с использованием рекурсии, которая принимает один аргумент:
    string — произвольная строка

Функция должна возвращать значение True, если переданная строка является палиндромом, или False в противном случае.

Примечание 1. Палиндром — текст, одинаково читающийся в обоих направлениях.
Примечание 2. Пустая строка является палиндромом, как и строка, состоящая из одного символа.

Sample Input 1:
print(is_palindrome('stepik'))

Sample Output 1:
False

Sample Input 2:
print(is_palindrome('level'))

Sample Output 2:
True

Sample Input 3:
print(is_palindrome('122333221'))

Sample Output 3:
True
"""


# 1
def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0].lower() != string[-1].lower():
        return False
    return is_palindrome(string[1:-1])

# 2
# def is_palindrome(word):
#     if len(word) <= 1:
#         return True
#     return (word[0] == word[-1]) and is_palindrome(word[1:-1])


print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
