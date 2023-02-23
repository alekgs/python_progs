"""
Загадка от Жака Фреско 🌶️

Однажды Жака Фреско спросили:
"Если ты такой умный, почему не богатый?"
Жак не стал отвечать на столь провокационный вопрос, вместо этого он задал загадку спрашивающему:
"Были разноцветные козлы. Сколько?"
"Сколько чего?"
"Сколько из них составляет более 7% от общего количества козлов?"


Вам доступен текстовый файл goats.txt в первой строке которого написано слово COLOURS, далее идет список всех
возможных цветов козлов. Затем идет строка со словом GOATS, и далее непосредственно перечисление козлов 
разных цветов. Перечень козлов включает только строки из первого списка.

Напишите программу создания файла answer.txt и вывода в него списка козлов, которые удовлетворяют условию
загадки от Жака Фреско.

Формат входных данных
На вход программе ничего не подается.

Формат выходных данных
Программа должна создать файл с именем answer.txt и вывести в него в алфавитном порядке названия цветов козлов,
которые удовлетворяют условию загадки Жака Фреско.

Примечание 1. Считайте, что исполняемая программа и указанные файлы находятся в одной папке.
Примечание 2. Если бы файл goats.txt содержал строки:

COLOURS
Pink goat
Green goat
Black goat
GOATS
Pink goat
Pink goat
Black goat
Pink goat
Pink goat
Black goat
Green goat
Pink goat
Black goat
Black goat
Pink goat
Pink goat
Black goat
Black goat
Pink goat

то файл answer.txt имел бы вид:
Black goat
Pink goat
"""

with open('goats.txt') as f_goats, open('answer.txt', 'w') as f_answer:
    # через словарь
    # goats = {}
    # for line in f_goats:
    #     goats[line.strip()] = goats.get(line.strip(), -1) + 1
    # total = sum(goats.values())
    #
    # for k, v in goats.items():
    #     if v > total * 0.07:
    #         f_answer.write(f'{k}\n')
    #

    # через множество
    s = f_goats.readlines()
    s = s[s.index("GOATS\n") + 1:]
    [f_answer.write(i) for i in sorted(set(s)) if s.count(i) / len(s) > 0.07]

    # через lambda
    # print(*filter(lambda x: s.count(x) / len(s) > 0.07, sorted(set(s))), file=f_answer, sep='')


