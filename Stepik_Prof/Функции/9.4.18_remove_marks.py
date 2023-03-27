"""
Функция remove_marks()

Реализуйте функцию remove_marks(), которая принимает два аргумента в следующем порядке:

    text — произвольная строка
    marks — набор символов

Функция должна возвращать строку text, предварительно удалив из нее все символы, перечисленные в
строке marks.

Также функция remove_marks() должна иметь атрибут count, представляющий собой количество вызовов
данной функции.

Примечание 1.
В тестирующую систему сдайте программу, содержащую только необходимую функцию remove_marks(),
но не код, вызывающий ее.


Sample Input 1:
text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)

Sample Output 1:
Hi Will we go together
1

Sample Input 2:
marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)

Sample Output 2:
Are you listening? Meet my family! There are my parents, my brother and me
Are you listening? Meet my family! There are my parents my brother and me.
Are you listening? Meet my family There are my parents, my brother and me.
Are you listening Meet my family! There are my parents, my brother and me.
4


1. Делаем по аналогии с прошлой задачей, добавляем атрибут count через setdefault('count',0)
2. Дальше заменяем элементы поштучно.
marks это строка, она итерируема, поэтому проходимся по этой строке.
for mark in marks:
    text = text.replace(mark,'')
3. прибавляем к уже созданному атрибуту count единицу.
4. выводим text
"""


def remove_marks(text, marks):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    return ''.join(s for s in text if s not in marks)


text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)


marks = '.,!?'
text = 'Are you listening? Meet my family! There are my parents, my brother and me.'

for mark in marks:
    print(remove_marks(text, mark))

print(remove_marks.count)
