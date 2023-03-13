# В таблицу attempt включить новую попытку для студента Баранова Павла по дисциплине «Основы баз данных».
# Установить текущую дату в качестве даты выполнения попытки.
USE online_test;

INSERT INTO
    attempt
    (student_id, subject_id, date_attempt)
    SELECT
        student_id,
        subject_id,
        CURDATE()
     FROM
         student,
         subject
     WHERE
        name_student LIKE 'Баран%' AND name_subject LIKE 'Основы баз%';


# Случайным образом выбрать три вопроса (запрос) по дисциплине, тестирование по которой собирается проходить
# студент, занесенный в таблицу attempt последним, и добавить их в таблицу testing.

# id последней попытки получить как максимальное значение id из таблицы attempt.

# Примечание:
# при выполнении запроса номера вставленных вопросов будут отличаться от образца, поскольку выбираются
# случайным образом.

# Query result:
# +------------+------------+-------------+-----------+
# | testing_id | attempt_id | question_id | answer_id |
# +------------+------------+-------------+-----------+
# | 1          | 1          | 9           | 25        |
# | 2          | 1          | 7           | 19        |
# | 3          | 1          | 6           | 17        |
# | 4          | 2          | 3           | 9         |
# | 5          | 2          | 1           | 2         |
# | 6          | 2          | 4           | 11        |
# | 7          | 3          | 6           | 18        |
# | 8          | 3          | 8           | 24        |
# | 9          | 3          | 9           | 28        |
# | 10         | 4          | 1           | 2         |
# | 11         | 4          | 5           | 16        |
# | 12         | 4          | 3           | 10        |
# | 13         | 5          | 2           | 6         |
# | 14         | 5          | 1           | 2         |
# | 15         | 5          | 4           | 12        |
# | 16         | 6          | 6           | 17        |
# | 17         | 6          | 8           | 22        |
# | 18         | 6          | 7           | 21        |
# | 19         | 7          | 1           | 3         |
# | 20         | 7          | 4           | 11        |
# | 21         | 7          | 5           | 16        |
# | 22         | 8          | 6           | NULL      |
# | 23         | 8          | 8           | NULL      |
# | 24         | 8          | 7           | NULL      |
# +------------+------------+-------------+-----------+

# INSERT INTO
#     testing
#     (attempt_id, question_id)
#     SELECT
#         attempt_id,
#         question_id
#     FROM
#         attempt at
#         JOIN question USING (subject_id)
#         JOIN subject sb ON
#             (
#               at.subject_id = sb.subject_id AND
#               (sb.subject_id, at.attempt_id) =
#                (
#                  SELECT
#                      subject_id, attempt_id
#                  FROM
#                      attempt
#                  WHERE
#                      date_attempt = (SELECT MAX(date_attempt) FROM attempt)
#                )
#             )
#     ORDER BY RAND()
#     LIMIT 3;

INSERT
    testing (attempt_id, question_id)
SELECT
    attempt_id,
    question_id
FROM
    attempt at
    JOIN question q ON
      attempt_id = (SELECT MAX(attempt_id) FROM attempt) AND
      q.subject_id = at.subject_id
ORDER BY
    RAND()
LIMIT 3;



# Студент прошел тестирование (то есть все его ответы занесены в таблицу testing), далее необходимо
# вычислить результат(запрос) и занести его в таблицу attempt для соответствующей попытки.
# Результат попытки вычислить как количество правильных ответов, деленное на 3
# (количество вопросов в каждой попытке) и умноженное на 100. Результат округлить до целого.
# Будем считать, что мы знаем id попытки,  для которой вычисляется результат, в нашем случае это 8.

# Query result:
# +------------+------------+------------+--------------+--------+
# | attempt_id | student_id | subject_id | date_attempt | result |
# +------------+------------+------------+--------------+--------+
# | 1          | 1          | 2          | 2020-03-23   | 67     |
# | 2          | 3          | 1          | 2020-03-23   | 100    |
# | 3          | 4          | 2          | 2020-03-26   | 0      |
# | 4          | 1          | 1          | 2020-04-15   | 33     |
# | 5          | 3          | 1          | 2020-04-15   | 67     |
# | 6          | 4          | 2          | 2020-04-21   | 100    |
# | 7          | 3          | 1          | 2020-05-17   | 33     |
# | 8          | 1          | 2          | 2020-06-12   | 67     |

# Пояснение
# Используйте вложенный запрос для вычисления результатов всех попыток по таблице testing, а в таблице
# attempt обновляйте только запись с id равным 8.


UPDATE attempt
    SET result =
        (
         SELECT
            ROUND(AVG(IFNULL(is_correct, 0)) * 100)
         FROM
            answer a
            JOIN testing t ON (a.answer_id = t.answer_id AND attempt_id = 8)
        )
    WHERE attempt_id = 8;



# Удалить из таблицы attempt все попытки, выполненные раньше 1 мая 2020 года.
# Также удалить и все соответствующие этим попыткам вопросы из таблицы testing.
#
# Query result:
# +------------+------------+------------+--------------+--------+
# | attempt_id | student_id | subject_id | date_attempt | result |
# +------------+------------+------------+--------------+--------+
# | 7          | 3          | 1          | 2020-05-17   | 33     |
# | 8          | 1          | 2          | 2020-06-12   | 67     |
# +------------+------------+------------+--------------+--------+

# Query result:
# +------------+------------+-------------+-----------+
# | testing_id | attempt_id | question_id | answer_id |
# +------------+------------+-------------+-----------+
# | 19         | 7          | 1           | 3         |
# | 20         | 7          | 4           | 11        |
# | 21         | 7          | 5           | 16        |
# | 22         | 8          | 7           | 19        |
# | 23         | 8          | 6           | 17        |
# | 24         | 8          | 8           | 22        |
# +------------+------------+-------------+-----------+

DELETE FROM attempt
WHERE date_attempt < STR_TO_DATE('01.05.2020', '%d.%m.%Y');



# Вы - хакер, жадный до сертификатов степика. Вы увидели структуру базы данных и решили себе сразу так
# заполучить ещё три  сертификата. (Сдача теста на 100 балов означает для вас новый сертификат).

# Ваша задача:
# 1. Добавьте себя любимого (любимую) в таблицу студентов.

# 2. Вставьте в таблицу attempt:
#  2.1  свой student_id,
#  2.2  все три предмета  которые вы якобы сдали.
#  2.3  случайную дату для каждой попытки, такую чтобы дата рассчитывалась как:
#  (сегодняшний день - случайное число дней от 1 до 12) . К примеру, если сегодня 15 января,
#  дата сдачи любого вашего теста была от 3 до 15 января, выбранная случайным образом.
#  Ибо система распознает жуликов, которые получают все три сертификата в один день.

# 2.4 В результат воткните себе 100 балов, чтобы все ботаны, кавказцы и евреи  обзавидовались,
# а ваша мамка расцвела от гордости за своего ребёнка.

# Примечания:
# п.2.2  - используйте функцию CROSS JOIN, вставляйте только SELECTOM
# вставлять словом values - ниже вашего достоинства.

# п. 2.3 - вычитать дату можно функцией
# DATE_ADD(NOW(), interval -10 DAY) # вернет дату, которая была 10 дней назад


/* Добавляем себя студентом */
INSERT INTO student (name_student) VALUES ('Степиков Хакер');

/* Проставляем 100 по всем предметам */
INSERT INTO
    attempt (student_id, subject_id, date_attempt, result)
SELECT
    (SELECT student_id FROM student WHERE name_student = 'Степиков Хакер'),
    subject_id,
    SUBDATE(CURDATE(), INTERVAL CEILING(MOD(RAND() * 100, 12)) DAY),
    100
FROM
    subject;

/* Выводим наглядную таблицу */
SELECT name_student, name_subject, date_attempt, result FROM attempt
JOIN student USING(student_id)
JOIN subject USING(subject_id);

# 2
INSERT INTO  student
SET name_student = 'Востров Стас';

INSERT INTO
    attempt (student_id, subject_id, date_attempt, result)
SELECT student_id,
       subject_id,
       DATE_ADD(CURDATE(), interval - (ROUND(RAND() * 11 + 1)) DAY) AS date,
       100
  FROM student
       CROSS JOIN subject ON name_student LIKE 'Востров С%'
 ORDER BY date;

SELECT * FROM student;