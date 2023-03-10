/*
Задание
Вывести название и автора тех книг, название которых состоит из двух и более слов, а инициалы автора содержат букву «С». Считать, что в названии слова отделяются друг от друга пробелами и не содержат знаков препинания, между фамилией автора и инициалами обязателен пробел, инициалы записываются без пробела в формате: буква, точка, буква, точка. Информацию отсортировать по названию книги в алфавитном порядке.

Результат:

+-----------------------+-------------+
| title                 | author      |
+-----------------------+-------------+
| Капитанская дочка     | Пушкин А.С. |
| Стихотворения и поэмы | Есенин С.А. |
+-----------------------+-------------+
Пояснение.
При записи условия, необходимо учесть, что слово в названии обязательно должно содержать  хотя бы один символ.
Инициалы в этом задании - это первая буква имени или отчества, после которой стоит точка.
Буква C должна быть написана в РУССКОЙ раскладке. Если не проходит решение - проверьте это.
Важно! Только для этого шага в таблицу добавлены новые записи.

*/

SELECT title, author
FROM book
WHERE
title LIKE "%_ %_%" AND
((author LIKE "_% С._.") OR
(author LIKE "_% _.С."))
ORDER BY title;