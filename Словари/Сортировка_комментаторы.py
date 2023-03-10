"""
Дили Вили Били

Дили Вили Били завели себе аккаунты в одной известной соцсети. Их страницы стали пользоваться популярностью и, 
конечно же, появились поклонники, оставляющие комментарии.  Ребята решили узнать у кого из них самое большое 
количество уникальных комментаторов. Ваша задача помочь им в этом и собрать нужную информацию.

Входные данные
В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора.
Комментаторы могут повторяться и комментировать разных персонажей 
Строка "конец" означает окончание ввода и встречается последней

Выходные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать внимания в этой задаче.
Гарантируется, что количество уникальных комментаторов у всех наших героев разное.
Могут быть ситуации, когда у героя нету ни единого комментатора, в таком случае
все равно нужно выводить информацию о нем.

Sample Input 1:

Дили: navalny
Дили: realdonaldtrump
Били: navalny
Вили: realdonaldtrump
Вили: realdonaldtrump
Били: joebiden
Дили: joebiden
конец

Sample Output 1:
Количество уникальных комментаторов у Дили - 3
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Вили - 1

Sample Input 2:
Дили: aaaa
Дили: aaaa
Били: aaaa
Дили: aaaa
Били: aaa
конец

Sample Output 2:
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Дили - 1
Количество уникальных комментаторов у Вили - 0
"""

sl = {'Дили': set(), 'Били': set(), 'Вили': set()}

for i in iter(input, 'конец'):
    name, comment = i.split(': ')
    sl[name].add(comment)

[print(f'Количество уник. комментаторов у {k}-{len(v)}') for k, v in sorted(sl.items(), key=lambda x: (-len(x[1])))]
