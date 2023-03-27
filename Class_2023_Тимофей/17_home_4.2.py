"""
Вводится строка с текстом. Требуется вывести все различные слова на экран одной строкой через пробел.

Ввод
one two one tho three

Вывод
one two tho three
"""
print(*sorted(set(input().split())))

