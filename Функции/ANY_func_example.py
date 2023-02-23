"""
О Ю Г Х Т
Кто не помнит со школьных уроков английского эту запоминашку для написания английский слов, таких как например bought.
Вашей программе на вход будут поступать слова, разделенные пробелом. Программа должна вывести True,
если встретилось хотя бы одно слово, заканчивающееся на ought. В противном случае нужно вывести False.

Регистр букв не имеет значения, значит интересующиеся нас слова могут заканчиваться как на ought,
так и например на OUGHT

Sample Input 1:
appendix expose ensure salon north

Sample Output 1:
False

Sample Input 2:
food forethought muscle stadium

Sample Output 2:
True
"""

print(any(s.endswith('ought') for s in input().lower().split()))
