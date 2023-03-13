CREATE TABLE author
    (
        author_id INT
            PRIMARY KEY AUTO_INCREMENT,
        name_author VARCHAR(50)
    );

INSERT INTO author (name_author)
VALUES ('Булгаков М.А.'),
       ('Достоевский Ф.М.'),
       ('Есенин С.А.'),
       ('Пастернак Б.Л.'),
       ('Лермонтов М.Ю.');

CREATE TABLE genre
    (
        genre_id INT
            PRIMARY KEY AUTO_INCREMENT,
        name_genre VARCHAR(30)
    );

INSERT INTO genre(name_genre)
VALUES ('Роман'),
       ('Поэзия'),
       ('Приключения');

CREATE TABLE book
    (
        book_id INT
            PRIMARY KEY AUTO_INCREMENT,
        title VARCHAR(50),
        author_id INT NOT NULL,
        genre_id INT,
        price DECIMAL(8, 2),
        amount INT,
        FOREIGN KEY (author_id) REFERENCES author (author_id) ON DELETE CASCADE,
        FOREIGN KEY (genre_id) REFERENCES genre (genre_id) ON DELETE SET NULL
    );

INSERT INTO book (title, author_id, genre_id, price, amount)
VALUES ('Мастер и Маргарита', 1, 1, 670.99, 3),
       ('Белая гвардия ', 1, 1, 540.50, 5),
       ('Идиот', 2, 1, 460.00, 10),
       ('Братья Карамазовы', 2, 1, 799.01, 2),
       ('Игрок', 2, 1, 480.50, 10),
       ('Стихотворения и поэмы', 3, 2, 650.00, 15),
       ('Черный человек', 3, 2, 570.20, 6),
       ('Лирика', 4, 2, 518.99, 2);

CREATE TABLE city
    (
        city_id INT
            PRIMARY KEY AUTO_INCREMENT,
        name_city VARCHAR(30),
        days_delivery INT
    );

INSERT INTO city(name_city, days_delivery)
VALUES ('Москва', 5),
       ('Санкт-Петербург', 3),
       ('Владивосток', 12);

CREATE TABLE client
    (
        client_id INT
            PRIMARY KEY AUTO_INCREMENT,
        name_client VARCHAR(50),
        city_id INT,
        email VARCHAR(30),
        FOREIGN KEY (city_id) REFERENCES city (city_id)
    );

INSERT INTO client(name_client, city_id, email)
VALUES ('Баранов Павел', 3, 'baranov@test'),
       ('Абрамова Катя', 1, 'abramova@test'),
       ('Семенонов Иван', 2, 'semenov@test'),
       ('Яковлева Галина', 1, 'yakovleva@test');

CREATE TABLE buy
    (
        buy_id INT
            PRIMARY KEY AUTO_INCREMENT,
        buy_description VARCHAR(100),
        client_id INT,
        FOREIGN KEY (client_id) REFERENCES client (client_id)
    );

INSERT INTO buy (buy_description, client_id)
VALUES ('Доставка только вечером', 1),
       (NULL, 3),
       ('Упаковать каждую книгу по отдельности', 2),
       (NULL, 1);

CREATE TABLE buy_book
    (
        buy_book_id INT
            PRIMARY KEY AUTO_INCREMENT,
        buy_id INT,
        book_id INT,
        amount INT,
        FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
        FOREIGN KEY (book_id) REFERENCES book (book_id)
    );

INSERT INTO buy_book(buy_id, book_id, amount)
VALUES (1, 1, 1),
       (1, 7, 2),
       (1, 3, 1),
       (2, 8, 2),
       (3, 3, 2),
       (3, 2, 1),
       (3, 1, 1),
       (4, 5, 1);

CREATE TABLE step
    (
        step_id INT
            PRIMARY KEY AUTO_INCREMENT,
        name_step VARCHAR(30)
    );

INSERT INTO step(name_step)
VALUES ('Оплата'),
       ('Упаковка'),
       ('Транспортировка'),
       ('Доставка');

CREATE TABLE buy_step
    (
        buy_step_id INT
            PRIMARY KEY AUTO_INCREMENT,
        buy_id INT,
        step_id INT,
        date_step_beg DATE,
        date_step_end DATE,
        FOREIGN KEY (buy_id) REFERENCES buy (buy_id),
        FOREIGN KEY (step_id) REFERENCES step (step_id)
    );

INSERT INTO buy_step(buy_id, step_id, date_step_beg, date_step_end)
VALUES (1, 1, '2020-02-20', '2020-02-20'),
       (1, 2, '2020-02-20', '2020-02-21'),
       (1, 3, '2020-02-22', '2020-03-07'),
       (1, 4, '2020-03-08', '2020-03-08'),
       (2, 1, '2020-02-28', '2020-02-28'),
       (2, 2, '2020-02-29', '2020-03-01'),
       (2, 3, '2020-03-02', NULL),
       (2, 4, NULL, NULL),
       (3, 1, '2020-03-05', '2020-03-05'),
       (3, 2, '2020-03-05', '2020-03-06'),
       (3, 3, '2020-03-06', '2020-03-10'),
       (3, 4, '2020-03-11', NULL),
       (4, 1, '2020-03-20', NULL),
       (4, 2, NULL, NULL),
       (4, 3, NULL, NULL),
       (4, 4, NULL, NULL);


USE book_shop;
SELECT *
  FROM book;

# Вывести фамилии всех клиентов, которые заказали книгу Булгакова «Мастер и Маргарита».
#
# Запрос:
#
# Этот запрос строится на основе нескольких таблиц, для удобства нужно определить фрагмент логической схемы базы данных,
# на основе которой строится запрос. В нашем случае выбираются название книги из таблицы book и фамилия клиента из
# таблицы client. Эти таблицы между собой непосредственно не связаны, поэтому нужно добавить «связующие» таблицы
# buy и buy_book:
#
# Для соединения этих таблиц используется INNER JOIN. Для удобства рекомендуется связи описывать последовательно:
# client → buy → buy_book → book.  А для соединения использовать пару первичный ключ и внешний ключ соответствующих
# таблиц. Например, соединение таблиц client и buy осуществляется по условию client.client_id = buy.client_id.

# Чтобы не усложнять схему, будем считать, что нам известен id Булгакова (это 1)
#
# SELECT DISTINCT name_client
# FROM
#     client
#     INNER JOIN buy ON client.client_id = buy.client_id
#     INNER JOIN buy_book ON buy_book.buy_id = buy.buy_id
#     INNER JOIN book ON buy_book.book_id=book.book_id
# WHERE title ='Мастер и Маргарита' and author_id = 1;
#
# В запросе отбираются уникальные клиенты (DISTINCT) так как один и тот же клиент мог заказать одну и ту же книгу несколько раз.
#
# Результат:
#
# +---------------+
# | name_client   |
# +---------------+
# | Баранов Павел |
# | Абрамова Катя |
# +---------------+


SELECT DISTINCT name_client
  FROM client
           JOIN buy
           ON client.client_id = buy.client_id
           JOIN buy_book
           ON buy_book.buy_id = buy.buy_id
           JOIN book
           ON buy_book.book_id = book.book_id
           JOIN author a
           ON a.author_id = book.author_id
 WHERE title = 'Мастер и Маргарита'
   AND a.name_author = 'Булгаков М.А.';

# Вывести все заказы Баранова Павла (id заказа, какие книги, по какой цене и в каком количестве он заказал)
# в отсортированном по номеру заказа и названиям книг виде.
#
# Если в нескольких таблицах столбцы называются одинаково – необходимо явно указывать из какой таблицы берется столбец.
# Например, столбец amount есть и в таблице book, и в таблице buy_book. В запросе нужно указать количество заказанных
# книг, то есть buy_book.amount.
#
# Связанные шаги
#     выборка столбцов;
#     соединение таблиц;
#     условие отбора (шаг, шаг);
#     сортировка.
#
# Результат
# +--------+--------------------+--------+--------+
# | buy_id | title              | price  | amount |
# +--------+--------------------+--------+--------+
# | 1      | Идиот              | 460.00 | 1      |
# | 1      | Мастер и Маргарита | 670.99 | 1      |
# | 1      | Черный человек     | 570.20 | 2      |
# | 4      | Игрок              | 480.50 | 1      |
# +--------+--------------------+--------+--------+


SELECT buy.buy_id, b.title, b.price, bb.amount
  FROM client c
           JOIN buy
           USING (client_id)
           JOIN buy_book bb
           USING (buy_id)
           JOIN book b
           USING (book_id)
           JOIN author a
           USING (author_id)
 WHERE c.name_client = 'Баранов Павел'
 ORDER BY buy.buy_id, b.title;

SELECT DISTINCT buy_id, title, price, buy_book.amount
  FROM book b
           JOIN buy_book
           USING (book_id)
           JOIN buy
           USING (buy_id)
           JOIN client
           USING (client_id)
 WHERE name_client = 'Баранов Павел'
 ORDER BY 1, 2;

SELECT buy.buy_id, title, price, buy_book.amount
  FROM (SELECT * FROM client WHERE name_client = 'Баранов Павел') AS cl
           JOIN buy
           ON cl.client_id = buy.client_id
           JOIN buy_book
           ON buy.buy_id = buy_book.buy_id
           JOIN book
           ON buy_book.book_id = book.book_id
 ORDER BY buy.buy_id, title;


# Посчитать, сколько раз была заказана каждая книга, для книги вывести ее автора
# (нужно посчитать, в каком количестве заказов фигурирует каждая книга).
# Вывести фамилию и инициалы автора, название книги, последний столбец назвать Количество.
# Результат отсортировать сначала  по фамилиям авторов, а потом по названиям книг.
#
# Для того, чтобы были выведены книги, которые клиенты не заказывали, использовать внешнее соединение.
# Связанные шаги
#
#     выборка столбцов и их именование;
#     соединение таблиц (шаг, шаг);
#     групповые функции;
#     сортировка.
#
# Результат
#
# +------------------+-----------------------+------------+
# | name_author      | title                 | Количество |
# +------------------+-----------------------+------------+
# | Булгаков М.А.    | Белая гвардия         | 1          |
# | Булгаков М.А.    | Мастер и Маргарита    | 2          |
# | Достоевский Ф.М. | Братья Карамазовы     | 0          |
# | Достоевский Ф.М. | Игрок                 | 1          |
# | Достоевский Ф.М. | Идиот                 | 2          |
# | Есенин С.А.      | Стихотворения и поэмы | 0          |
# | Есенин С.А.      | Черный человек        | 1          |
# | Пастернак Б.Л.   | Лирика                | 1          |
# +------------------+-----------------------+------------+

SELECT name_author, title, COUNT(buy_book.amount) AS количество
  FROM book
           JOIN author
           USING (author_id)
           LEFT JOIN buy_book
           USING (book_id)
 GROUP BY name_author, title
 ORDER BY name_author, title;

SELECT name_author, title, COUNT(buy_book.amount) AS количество
  FROM author
           JOIN book
           USING (author_id)
           LEFT JOIN buy_book
           USING (book_id)
 GROUP BY book.title, name_author
 ORDER BY name_author, title;

# Вывести города, в которых живут клиенты, оформлявшие заказы в интернет-магазине.
# Указать количество заказов в каждый город, этот столбец назвать Количество.
# Информацию вывести по убыванию количества заказов, а затем в алфавитном порядке по названию городов.

# Связанные шаги
#
#     выборка столбцов и их именование;
#     соединение таблиц;
#     сортировка.
#
# Результат
#
# +-----------------+------------+
# | name_city       | Количество |
# +-----------------+------------+
# | Владивосток     | 2          |
# | Москва          | 1          |
# | Санкт-Петербург | 1          |
# +-----------------+------------+

SELECT name_city, COUNT(buy_id) AS количество
  FROM client
           JOIN city
           USING (city_id)
           JOIN buy
           USING (client_id)
 GROUP BY name_city
 ORDER BY количество DESC, name_city;


# Вывести номера всех оплаченных заказов и даты, когда они были оплачены.
#

# Пояснение
# С каждым заказом в таблице buy_step связаны 4 записи, которые фиксируют этапы  заказа.
# Для каждого заказа сначала выставляется счет на оплату ( в запись с step_id со значением 1 («Оплата»)
# в столбец date_step_beg заносится  дата выставления счета по заказу ). После того, как счет оплачен, в столбец
# date_step_end той же записи заносится дата оплаты заказа.
# Затем в таблице  buy_step заполняется  step_id со значением 2 («Упаковка»)  для текущего заказа:
# после передачи заказа на упаковку заполняется поле date_step_beg, а после окончания упаковки – поле date_step_end.
# И так далее для оставшихся двух шагов («Транспортировка» и «Доставка»).

# Для реализации запроса учитывать тот факт, что те заказы, которые не оплачены в таблице buy_step в записи с step_id
# со значением 1 («Оплата»)  в столбце date_step_end  имеют значение Null.

# Связанные шаги
#     выборка столбцов;
#     соединение таблиц;
#     сравнение с пустым значением;
#     условие отбора (шаг, шаг);
#     сортировка.

# Результат
#
# +--------+---------------+
# | buy_id | date_step_end |
# +--------+---------------+
# | 1      | 2020-02-20    |
# | 2      | 2020-02-28    |
# | 3      | 2020-03-05    |
# +--------+---------------+
#

SELECT buy_id, date_step_end
  FROM step
           JOIN buy_step bs
           USING (step_id)
 WHERE step_id = 1
   AND date_step_end;

SELECT buy_id, date_step_end
  FROM buy_step
 WHERE step_id = 1
   AND date_step_end;



# Вывести информацию о каждом заказе: его номер, кто его сформировал (фамилия пользователя) и # его стоимость
# (сумма произведений количества заказанных книг и их цены), в отсортированном по номеру заказа виде.
# Последний столбец назвать Стоимость.
#
# Результат
#
# +--------+----------------+-----------+
# | buy_id | name_client    | Стоимость |
# +--------+----------------+-----------+
# | 1      | Баранов Павел  | 2271.39   |
# | 2      | Семенонов Иван | 1037.98   |
# | 3      | Абрамова Катя  | 2131.49   |
# | 4      | Баранов Павел  | 480.50    |
# +--------+----------------+-----------+

SELECT buy_id, name_client, SUM(bb.amount * price) AS стоимость
  FROM buy
           JOIN client
           USING (client_id)
           JOIN buy_book bb
           USING (buy_id)
           JOIN book
           USING (book_id)
 GROUP BY buy_id, name_client
 ORDER BY buy_id;



# Вывести номера заказов (buy_id) и названия этапов, на которых они в данный момент находятся.
# Если заказ доставлен –  информацию о нем не выводить. Информацию отсортировать по возрастанию
# buy_id.

# Результат
#
# +--------+-----------------+
# | buy_id | name_step       |
# +--------+-----------------+
# | 2      | Транспортировка |
# | 3      | Доставка        |
# | 4      | Оплата          |
# +--------+-----------------+

SELECT buy_id, name_step
  FROM buy_step
           JOIN step
           USING (step_id)
 WHERE buy_step.date_step_beg
   AND date_step_end IS NULL
 GROUP BY buy_id, name_step
 ORDER BY buy_id;



# В таблице city для каждого города указано количество дней, за которые заказ может быть доставлен в этот
# город (рассматривается только этап "Транспортировка"). Для тех заказов, которые прошли этап
# транспортировки,  вывести количество дней за которое заказ реально доставлен в город.
# А также, если заказ доставлен с опозданием, указать количество дней задержки, в противном случае вывести 0.
# В результат включить  номер заказа (buy_id), а также вычисляемые столбцы Количество_дней и Опоздание.

# Информацию вывести  в отсортированном по номеру заказа виде.

# Результат
# +--------+-----------------+-----------+
# | buy_id | Количество_дней | Опоздание |
# +--------+-----------------+-----------+
# | 1      | 14              | 2         |
# | 3      | 4               | 0         |
# +--------+-----------------+-----------+

# Пояснение
#  Для вычисления поля «Опоздание» используйте функцию if(), а для вычисления разности дат – функцию
#  DATEDIFF().
#  Если доставка еще не осуществлена, то поле date_step_end  для этапа Транспортировка - пусто.

SELECT buy_id, DATEDIFF(date_step_end, date_step_beg) AS количество_дней,
       GREATEST((SELECT количество_дней) - days_delivery, 0) AS опоздание
  FROM buy_step
           JOIN step
           USING (step_id)
           JOIN buy
           USING (buy_id)
           JOIN client
           USING (client_id)
           JOIN city
           USING (city_id)
 WHERE step_id = 3
   AND date_step_end;


# Выбрать всех клиентов, которые заказывали книги Достоевского, информацию вывести в отсортированном
# по # алфавиту виде.
# В решении используйте фамилию автора, а не его id.
#
# Результат
# +---------------+
# | name_client   |
# +---------------+
# | Абрамова Катя |
# | Баранов Павел |
# +---------------+

SELECT name_client
  FROM client
           JOIN buy
           USING (client_id)
           JOIN buy_book
           USING (buy_id)
           JOIN book
           USING (book_id)
           JOIN author
           USING (author_id)
 WHERE name_author = 'Достоевский Ф.М.'
 GROUP BY name_client
 ORDER BY name_client;


# Вывести жанр (или жанры), в котором было заказано больше всего экземпляров книг, указать это количество.
# Последний столбец назвать Количество.
#
# Результат
#
# +------------+------------+
# | name_genre | Количество |
# +------------+------------+
# | Роман      | 7          |
# +------------+------------+

# Пояснение
#
# Использовать вложенный запрос для вычисления максимального значения экземпляров книг.
# Рекомендуется запрос реализовывать по шагам.
#
# Связанные шаги
#     выборка столбцов и их именование;
#     соединение таблиц;
#     групповые функции(шаг, шаг);
#     групповые вычисления по всей таблице;
#     вложенные запросы в условии отбора;
#     вложенные запросы в операторах соединения.
#

SELECT name_genre, SUM(buy_book.amount) AS количество
  FROM genre
           JOIN book
           USING (genre_id)
           JOIN buy_book
           USING (book_id)
 GROUP BY name_genre
HAVING количество = (SELECT MAX(sum_amount)
                       FROM (SELECT SUM(bb.amount) AS sum_amount
                               FROM book
                                        JOIN buy_book bb
                                        USING (book_id)
                              GROUP BY genre_id) AS q_max);



# Сравнить ежемесячную выручку от продажи книг за текущий и предыдущий годы.
# Для этого вывести год, месяц, сумму выручки в отсортированном сначала по возрастанию месяцев,
# затем по возрастанию лет виде. Название столбцов: Год, Месяц, Сумма.

# Фрагмент логической схемы базы данных (в запросе НЕ ОБЯЗАТЕЛЬНО использовать все таблицы):

# Информация о продажах предыдущего года хранится в архивной таблице buy_archive, которая создается в конце
# года на основе информации из таблиц базы данных и имеет следующую структуру:
#
# buy_archive_id ключевой столбец
# buy_id 	 id заказов, выбирается из таблицы buy
# client_id 	 id клиентов, выбирается из из таблицы client
# book_id 	 id книги, выбирается из таблицы book
# date_payment 	 дата оплаты заказа, выбирается из столбца date_step_end таблицы buy_step этапа «Оплата»
#                соответствующего заказа
# price 	 цена книги в текущем заказе из таблицы book (хранится, так как цена может измениться)
# amount 	 количество купленных книг в текущем заказе, из таблицы buy_book

DROP TABLE IF EXISTS buy_archive;

CREATE TABLE buy_archive
    (
        buy_archive_id INT
            PRIMARY KEY AUTO_INCREMENT,
        buy_id INT,
        client_id INT,
        book_id INT,
        date_payment DATE,
        price DECIMAL(8, 2),
        amount INT
    );

INSERT INTO buy_archive (buy_id, client_id, book_id, date_payment, amount, price)
VALUES (2, 1, 1, '2019-02-21', 2, 670.60),
       (2, 1, 3, '2019-02-21', 1, 450.90),
       (1, 2, 2, '2019-02-10', 2, 520.30),
       (1, 2, 4, '2019-02-10', 3, 780.90),
       (1, 2, 3, '2019-02-10', 1, 450.90),
       (3, 4, 4, '2019-03-05', 4, 780.90),
       (3, 4, 5, '2019-03-05', 2, 480.90),
       (4, 1, 6, '2019-03-12', 1, 650.00),
       (5, 2, 1, '2019-03-18', 2, 670.60),
       (5, 2, 4, '2019-03-18', 1, 780.90);

# Вывести всех клиентов, которые делали заказы или в этом, или в предыдущем году.

SELECT name_client
  FROM buy_archive
           INNER JOIN client
           USING (client_id)
 UNION
SELECT name_client
  FROM buy
           INNER JOIN client
           USING (client_id);

# Вывести информацию об оплаченных заказах за предыдущий и текущий год, информацию отсортировать по
# name_client.

SELECT buy_id, c.name_client, book_id, date_payment, amount, price
  FROM buy_archive,
       client AS c
 WHERE buy_archive.client_id = c.client_id
 UNION ALL
SELECT buy.buy_id, name_client, book_id, date_step_end, buy_book.amount, price
  FROM book
           JOIN buy_book
           USING (book_id)
           JOIN buy
           USING (buy_id)
           JOIN buy_step
           USING (buy_id)
           JOIN step
           USING (step_id)
           JOIN client
           USING (client_id)
 WHERE date_step_end
   AND step_id = 1
 ORDER BY name_client;



# Сравнить ежемесячную выручку от продажи книг за текущий и предыдущий годы.
# Для этого вывести год, месяц, сумму выручки в отсортированном сначала по возрастанию месяцев,
# затем по возрастанию лет виде.

# Название столбцов: Год, Месяц, Сумма.

# Пояснение
#    Ежемесячная выручка рассчитывается как сумма произведений цены книги на заказанное пользователем в
#    этом месяце количество.
#    Цена книги для текущего года хранится в таблице book, а для предыдущего в buy_archive.
#    Функция для выделения месяца рассмотрена на этом шаге.

# Результат
#
# +------+----------+---------+
# | Год  | Месяц    | Сумма   |
# +------+----------+---------+
# | 2019 | February | 5626.30 |
# | 2020 | February | 3309.37 |
# | 2019 | March    | 6857.50 |
# | 2020 | March    | 2131.49 |
# +------+----------+---------+

SELECT
    Год, Месяц, SUM(S) AS Сумма
  FROM
      (SELECT
          YEAR(date_step_end) AS Год,
          MONTHNAME(date_step_end) AS Месяц,
          SUM(price * bb.amount) AS S
          FROM
              book
              JOIN buy_book bb USING (book_id)
              JOIN buy_step USING (buy_id)
         WHERE
             step_id = 1 AND date_step_end
         GROUP BY
             price, bb.amount, date_step_end

        UNION ALL

         SELECT
             YEAR(date_payment) AS Год,
             MONTHNAME(date_payment) AS Месяц,
             SUM(price * amount) AS S
           FROM
             buy_archive
           WHERE
             date_payment IS NOT NULL
           GROUP BY
             price, amount, date_payment) AS query
 GROUP BY
     Год, Месяц
 ORDER BY
     Месяц, Год;



# Вывести клиентов, которые делали покупки в прошлом году, но не делали в этом.
# А также новых клиентов, которые делали заказы только в текущем году.
# Информацию отсортировать по возрастанию лет.

# Шаг 1. Отберем клиентов прошлого года, указав дату самого раннего заказа, а также клиентов этого года,
# указав для них самую раннюю дату оплаты заказа.

SELECT name_client, MIN(date_payment) AS first_payment
FROM
    buy_archive
    INNER JOIN client USING(client_id)
GROUP BY  name_client
UNION
SELECT name_client, MIN(date_step_end)
FROM
    buy
    INNER JOIN client USING(client_id)
    INNER JOIN buy_step USING(buy_id)
GROUP BY name_client;

# Результат:
#
# +-----------------+---------------+
# | name_client     | first_payment |
# +-----------------+---------------+
# | Абрамова Катя   | 2019-02-10    |
# | Баранов Павел   | 2019-02-21    |
# | Яковлева Галина | 2019-03-05    |
# | Абрамова Катя   | 2020-03-05    |
# | Баранов Павел   | 2020-02-20    |
# | Семенонов Иван  | 2020-02-28    |
# +-----------------+---------------+

# Как видно из таблицы, некоторые клиенты делали покупки как в прошлом, так и в этом году.
# Они встречаются в таблице 2 раза.

# Шаг 2. Оставим только тех клиентов, которые встречаются в полученной таблице один раз,
# для этого используем предыдущий запрос как вложенный.

SELECT
       name_client,
       MIN(YEAR(first_payment)) AS Год
FROM
  (
   SELECT
       name_client,
       MIN(date_payment) AS first_payment
   FROM
       buy_archive
       INNER JOIN client USING(client_id)
   GROUP BY name_client

   UNION

   SELECT
       name_client, MIN(date_step_end)
   FROM
       buy
       INNER JOIN client USING(client_id)
       INNER JOIN buy_step USING (buy_id)
   GROUP BY
       name_client
  ) query_in
GROUP BY name_client
HAVING COUNT(*) = 1
ORDER BY Год;

# Результат:
#
# +-----------------+------+
# | name_client     | Год  |
# +-----------------+------+
# | Яковлева Галина | 2019 |
# | Семенонов Иван  | 2020 |
# +-----------------+------+

# Для каждой отдельной книги необходимо вывести информацию о количестве проданных экземпляров
# и их стоимости за 2020 и 2019 год.
# Вычисляемые столбцы назвать Количество и Сумма.
# Информацию отсортировать по убыванию стоимости.

# Пояснение
# При вычислении Количества и Суммы для текущего года учитывать только те книги, которые уже оплачены
# (указана дата оплаты для шага "Оплата" в таблице buy_step).
# Результат

# +-----------------------+------------+---------+
# | title                 | Количество | Сумма   |
# +-----------------------+------------+---------+
# | Братья Карамазовы     | 8          | 6247.20 |
# | Мастер и Маргарита    | 6          | 4024.38 |
# | Идиот                 | 5          | 2281.80 |
# | Белая гвардия         | 3          | 1581.10 |
# | Черный человек        | 2          | 1140.40 |
# | Лирика                | 2          | 1037.98 |
# | Игрок                 | 2          | 961.80  |
# | Стихотворения и поэмы | 1          | 650.00  |
# +-----------------------+------------+---------+
SELECT
       title,
       SUM(A) AS Количество,
       SUM(S) AS Сумма
FROM
    book
    JOIN
     (SELECT
        book_id,
        SUM(ba.amount) AS A,
        SUM(ba.amount * ba.price) AS S
     FROM
        buy_archive ba
        JOIN book USING(book_id)
     GROUP BY
        book_id
     UNION ALL
        SELECT
            book_id,
            SUM(bb.amount) AS A,
            SUM(bb.amount * price) AS S
        FROM
            book
            JOIN buy_book bb USING(book_id)
            JOIN buy_step USING (buy_id)
        WHERE
            step_id = 1 AND date_step_end
        GROUP BY
            book_id) as query USING(book_id)
GROUP BY
    title
ORDER BY
    Сумма DESC;


# Вывести названия книг, которые ни разу не были заказаны в текущем году (2020),
# отсортировав в алфавитном порядке.

SELECT
    book.title
FROM
    book
LEFT JOIN
        buy_book USING(book_id)
WHERE
    buy_book.amount IS NULL
ORDER BY 1;

# select title
# from book
# where book_id not in (
#     select book_id
#     from buy_book
#     -- УЧИТЫВАТЬ ОПЛАТУ
#         join buy_step using (buy_id)
#     where step_id = 1 and date_step_end is not null
#     -- УЧИТЫВАТЬ АРХИВ
#     union
#     select book_id
#     from buy_archive
# )
# order by 1