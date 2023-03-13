CREATE DATABASE abiturient;

USE abiturient;

START TRANSACTION;
DROP TABLE IF EXISTS enrollee_subject;
DROP TABLE IF EXISTS program_enrollee;
DROP TABLE IF EXISTS program_subject;
DROP TABLE IF EXISTS enrollee_achievement;
DROP TABLE IF EXISTS achievement;
DROP TABLE IF EXISTS enrollee;
DROP TABLE IF EXISTS program;
DROP TABLE IF EXISTS subject;
DROP TABLE IF EXISTS department;
COMMIT;

START TRANSACTION ;
CREATE TABLE department (
    `department_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name_department` VARCHAR(30)
);
INSERT INTO department (`department_id`, `name_department`)
VALUES (1, 'Инженерная школа'), (2, 'Школа естественных наук');

CREATE TABLE subject (
    `subject_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name_subject` VARCHAR(30)
);
INSERT INTO subject (`subject_id`, `name_subject`)
VALUES (1, 'Русский язык'), (2, 'Математика'), (3, 'Физика'), (4, 'Информатика');

CREATE TABLE program (
    `program_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name_program` VARCHAR(50),
    `department_id` INT,
    `plan` INT,
    FOREIGN KEY (`department_id`) REFERENCES `department`(`department_id`) ON DELETE CASCADE
);
INSERT INTO program (`program_id`, `name_program`, `department_id`, `plan`)
VALUES (1, 'Прикладная математика и информатика', 2, 2),
(2, 'Математика и компьютерные науки', 2, 1),
(3, 'Прикладная механика', 1, 2),
(4, 'Мехатроника и робототехника', 1, 3);

CREATE TABLE enrollee (
    `enrollee_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name_enrollee` VARCHAR(50)
);
INSERT INTO enrollee (`enrollee_id`, `name_enrollee`)
VALUES (1, 'Баранов Павел'), (2, 'Абрамова Катя'), (3, 'Семенов Иван'),
(4, 'Яковлева Галина'), (5, 'Попов Илья'), (6, 'Степанова Дарья');

CREATE TABLE achievement (
    `achievement_id` INT PRIMARY KEY AUTO_INCREMENT,
    `name_achievement` VARCHAR(30),
    `bonus` INT
);
INSERT INTO achievement (`achievement_id`, `name_achievement`, `bonus`)
VALUES (1, 'Золотая медаль', 5), (2, 'Серебряная медаль', 3),
    (3, 'Золотой значок ГТО', 3),(4, 'Серебряный значок ГТО', 1);

CREATE TABLE enrollee_achievement (
    `enrollee_achiev_id` INT PRIMARY KEY AUTO_INCREMENT,
    `enrollee_id` INT,
    `achievement_id` INT,
    FOREIGN KEY (`enrollee_id`) REFERENCES `enrollee`(`enrollee_id`) ON DELETE CASCADE,
    FOREIGN KEY (`achievement_id`) REFERENCES `achievement`(`achievement_id`) ON DELETE CASCADE
);
INSERT INTO enrollee_achievement (`enrollee_achiev_id`, `enrollee_id`, `achievement_id`)
VALUES (1, 1, 2), (2, 1, 3), (3, 3, 1), (4, 4, 4), (5, 5, 1),(6, 5, 3);

CREATE TABLE program_subject (
    `program_subject_id` INT PRIMARY KEY AUTO_INCREMENT,
    `program_id` INT,
    `subject_id` INT,
    `min_result` INT,
    FOREIGN KEY (`program_id`) REFERENCES `program`(`program_id`)  ON DELETE CASCADE,
    FOREIGN KEY (`subject_id`) REFERENCES `subject`(`subject_id`) ON DELETE CASCADE
);
INSERT INTO program_subject (`program_subject_id`, `program_id`, `subject_id`, `min_result`)
VALUES (1, 1, 1, 40),(2, 1, 2, 50), (3, 1, 4, 60), (4, 2, 1, 30),
       (5, 2, 2, 50),(6, 2, 4, 60), (7, 3, 1, 30),(8, 3, 2, 45),
       (9, 3, 3, 45),(10, 4, 1, 40), (11, 4, 2, 45), (12, 4, 3, 45);

CREATE TABLE program_enrollee (
    `program_enrollee_id` INT PRIMARY KEY AUTO_INCREMENT,
    `program_id` INT,
    `enrollee_id` INT,
    FOREIGN KEY (`program_id`) REFERENCES `program`(`program_id`) ON DELETE CASCADE,
    FOREIGN KEY (`enrollee_id`) REFERENCES enrollee(`enrollee_id`) ON DELETE CASCADE
);
INSERT INTO program_enrollee (`program_enrollee_id`, `program_id`, `enrollee_id`)
VALUES (1, 3, 1), (2, 4, 1), (3, 1, 1), (4, 2, 2), (5, 1, 2),
       (6, 1, 3), (7, 2, 3), (8, 4, 3), (9, 3, 4), (10, 3, 5),
       (11, 4, 5), (12, 2, 6), (13, 3, 6), (14, 4, 6);

CREATE TABLE enrollee_subject (
    `enrollee_subject_id` INT PRIMARY KEY AUTO_INCREMENT,
    `enrollee_id` INT,
    `subject_id` INT,
    `result` INT,
    FOREIGN KEY (`enrollee_id`) REFERENCES `enrollee`(`enrollee_id`) ON DELETE CASCADE,
    FOREIGN KEY (`subject_id`) REFERENCES `subject`(`subject_id`) ON DELETE CASCADE
);
INSERT INTO enrollee_subject (`enrollee_subject_id`, `enrollee_id`, `subject_id`, `result`)
VALUES (1, 1, 1, 68), (2, 1, 2, 70), (3, 1, 3, 41), (4, 1, 4, 75), (5, 2, 1, 75), (6, 2, 2, 70),
       (7, 2, 4, 81), (8, 3, 1, 85), (9, 3, 2, 67), (10, 3, 3, 90), (11, 3, 4, 78), (12, 4, 1, 82),
       (13, 4, 2, 86), (14, 4, 3, 70), (15, 5, 1, 65), (16, 5, 2, 67), (17, 5, 3, 60),
       (18, 6, 1, 90), (19, 6, 2, 92), (20, 6, 3, 88), (21, 6, 4, 94);
COMMIT;

USE abiturient;



#
# Вывести абитуриентов, которые хотят поступать на образовательную программу «Мехатроника и робототехника» в
# отсортированном по фамилиям виде.

# Результат
# +-----------------+
# | name_enrollee   |
# +-----------------+
# | Баранов Павел   |
# | Попов Илья      |
# | Семенов Иван    |
# | Степанова Дарья |
# +-----------------+

SELECT
    name_enrollee
FROM
    enrollee
       JOIN program_enrollee pe USING (enrollee_id)
       JOIN program p ON
            pe.program_id = p.program_id AND
            p.name_program LIKE 'Мехатр%'
ORDER BY 1;

# Вывести образовательные программы, на которые для поступления необходим предмет «Информатика».
# Программы отсортировать в обратном алфавитном порядке.
#
# Результат
#
# +-------------------------------------+
# | name_program                        |
# +-------------------------------------+
# | Прикладная математика и информатика |
# | Математика и компьютерные науки     |
# +-------------------------------------+

SELECT
    name_program
FROM
    program
    JOIN program_subject ps USING (program_id)
    JOIN subject s ON
        ps.subject_id = s.subject_id AND
        s.name_subject = 'Информатика'
ORDER BY 1 DESC;



# Выведите количество абитуриентов, сдавших ЕГЭ по каждому предмету,
# максимальное, минимальное и среднее значение баллов по предмету ЕГЭ.

# Вычисляемые столбцы назвать Количество, Максимум, Минимум, Среднее.
# Информацию отсортировать по названию предмета в алфавитном порядке,
# среднее значение округлить до одного знака после запятой.

# Результат
#
# +--------------+------------+----------+---------+---------+
# | name_subject | Количество | Максимум | Минимум | Среднее |
# +--------------+------------+----------+---------+---------+
# | Информатика  | 4          | 94       | 75      | 82.0    |
# | Математика   | 6          | 92       | 67      | 75.3    |
# | Русский язык | 6          | 90       | 65      | 77.5    |
# | Физика       | 5          | 90       | 41      | 69.8    |
# +--------------+------------+----------+---------+---------+


SELECT
    name_subject,
    COUNT(*) AS Количество,
    MAX(result) AS Максимум,
    MIN(result) AS Минимум,
    ROUND(AVG(result),1) AS Среднее
FROM
    subject
    JOIN enrollee_subject USING (subject_id)
GROUP BY
    name_subject
ORDER BY 1;



# Вывести образовательные программы, для которых минимальный балл ЕГЭ по каждому предмету больше или равен 40 баллам.
# Программы вывести в отсортированном по алфавиту виде.

# Результат
# +-------------------------------------+
# | name_program                        |
# +-------------------------------------+
# | Мехатроника и робототехника         |
# | Прикладная математика и информатика |
# +-------------------------------------+

SELECT
    name_program
FROM
    program
    JOIN program_subject USING (program_id)
GROUP BY
    name_program HAVING MIN(min_result) >= 40
ORDER BY 1;


# Вывести образовательные программы, которые имеют самый большой план набора, вместе с этой величиной.
# Результат
# +-----------------------------+------+
# | name_program                | plan |
# +-----------------------------+------+
# | Мехатроника и робототехника | 3    |
# +-----------------------------+------+

SELECT
    name_program,
    plan
FROM
    program
WHERE
    plan = (SELECT MAX(plan) FROM program);



# Посчитать, сколько дополнительных баллов получит каждый абитуриент.
# Столбец с дополнительными баллами назвать Бонус.
# Информацию вывести в отсортированном по фамилиям виде.

# Результат
# +-----------------+-------+
# | name_enrollee   | Бонус |
# +-----------------+-------+
# | Абрамова Катя   | 0     |
# | Баранов Павел   | 6     |
# | Попов Илья      | 8     |
# | Семенов Иван    | 5     |
# | Степанова Дарья | 0     |
# | Яковлева Галина | 1     |
# +-----------------+-------+

# Пояснение

# Чтобы включить в результирующую таблицу всех абитуриентов, а не только тех, у кого есть дополнительные баллы,
# используйте оператор внешнего соединения.

# После использования оператора внешнего соединения, у тех абитуриентов, у которых нет дополнительных баллов, в
# столбец «Бонус» будет занесено значение Null (на Stepik отображается None). Включите в запрос функцию if(),
# которая будет сравнивать сумму баллов с Null и,  если сравнение верно, то заносить 0, в противном случае – сумму баллов.


SELECT
    name_enrollee,
    IFNULL(SUM(bonus), 0) AS Бонус
FROM
    enrollee
    LEFT JOIN enrollee_achievement USING (enrollee_id)
    LEFT JOIN achievement USING (achievement_id)
GROUP BY
    name_enrollee
ORDER BY 1;



# Выведите сколько человек подало заявление на каждую образовательную программу и конкурс на нее (число поданных
# заявлений деленное на количество мест по плану), округленный до 2-х знаков после запятой.

# В запросе вывести название факультета, к которому относится образовательная программа,
# название образовательной программы, план набора абитуриентов на образовательную программу (plan),
# количество поданных заявлений (Количество) и Конкурс. Информацию отсортировать в порядке убывания конкурса.

# Результат
#
# +-------------------------+-------------------------------------+------+------------+---------+
# | name_department         | name_program                        | plan | Количество | Конкурс |
# +-------------------------+-------------------------------------+------+------------+---------+
# | Школа естественных наук | Математика и компьютерные науки     | 1    | 3          | 3.00    |
# | Инженерная школа        | Прикладная механика                 | 2    | 4          | 2.00    |
# | Школа естественных наук | Прикладная математика и информатика | 2    | 3          | 1.50    |
# | Инженерная школа        | Мехатроника и робототехника         | 3    | 4          | 1.33    |
# +-------------------------+-------------------------------------+------+------------+---------+


# Пояснение
# После GROUP BY задаются ВСЕ столбцы, указанные после SELECT,  к которым не применяются групповые функции или
# выражения с групповыми функциями. В этом запросе это name_department, name_program и plan.

SELECT name_department,
       name_program,
       plan,
       COUNT(pe.enrollee_id) AS Количество,
       ROUND(COUNT(pe.enrollee_id) / plan, 2) AS Конкурс
FROM
    program
    JOIN department USING (department_id)
    JOIN program_enrollee pe USING (program_id)
GROUP BY
    name_department,
    name_program,
    plan
ORDER BY
    Конкурс DESC;

# Вывести образовательные программы, на которые для поступления необходимы предмет «Информатика» и «Математика»
# в отсортированном по названию программ виде.

# Результат
# +-------------------------------------+
# | name_program                        |
# +-------------------------------------+
# | Математика и компьютерные науки     |
# | Прикладная математика и информатика |
# +-------------------------------------+


# Пояснение
# Сначала отберите все  программы, для которых определены Математика или Информатика, а потом, сгруппировав результат,
# отберите те программы, у которых количество отобранных дисциплин ровно две.

SELECT name_program
FROM
      program
      JOIN program_subject ps USING (program_id)
      JOIN subject s ON
           ps.subject_id = s.subject_id AND
           name_subject IN ('Информатика', 'Математика')
GROUP BY name_program
HAVING COUNT(name_program) = 2
# HAVING SUM(name_subject IN ('Информатика', 'Математика')) = 2
ORDER BY 1;



# Посчитать количество баллов каждого абитуриента на каждую образовательную программу,
# на которую он подал заявление, по результатам ЕГЭ.

# В результат включить название образовательной программы, фамилию и имя абитуриента,
# а также столбец с суммой баллов, который назвать itog.
#
# Информацию вывести в отсортированном сначала по образовательной программе, а потом по убыванию суммы баллов виде.

#Результат
#
# +-------------------------------------+-----------------+------+
# | name_program                        | name_enrollee   | itog |
# +-------------------------------------+-----------------+------+
# | Математика и компьютерные науки     | Степанова Дарья | 276  |
# | Математика и компьютерные науки     | Семенов Иван    | 230  |
# | Математика и компьютерные науки     | Абрамова Катя   | 226  |
# | Мехатроника и робототехника         | Степанова Дарья | 270  |
# | Мехатроника и робототехника         | Семенов Иван    | 242  |
# | Мехатроника и робототехника         | Попов Илья      | 192  |
# | Мехатроника и робототехника         | Баранов Павел   | 179  |
# | Прикладная математика и информатика | Семенов Иван    | 230  |
# | Прикладная математика и информатика | Абрамова Катя   | 226  |
# | Прикладная математика и информатика | Баранов Павел   | 213  |
# | Прикладная механика                 | Степанова Дарья | 270  |
# | Прикладная механика                 | Яковлева Галина | 238  |
# | Прикладная механика                 | Попов Илья      | 192  |
# | Прикладная механика                 | Баранов Павел   | 179  |
# +-------------------------------------+-----------------+------+

# Пояснение

# При описании соединения таблиц можно использовать схему enrollee →program_enrollee→program →program_subject →subject
# →enrollee_subject. Следующей для соединения идет таблица enrollee , но она уже в списке есть. Поэтому для последнего
# соединения subject →enrollee_subject нужно использовать дополнительное условие связи между enrollee_subject и enrollee:
#
# subject.subject_id = enrollee_subject.subject_id
# and enrollee_subject.enrollee_id = enrollee.enrollee_id
#
# Важно! Можно использовать и другие способы соединения таблиц.
# Подробное объяснение, зачем нужно дополнительное условие для соединения предложила Lidiya Ribakova:

# Если не использовать это условие, "не сходятся данные, например, по Степанова Дарья и Семенов Иван, так как они
# сдали 4 ЕГЭ, а для поступления нужны только 3 предмета, то есть надо из 4 суммировать только 3. И вот как раз в
# таблице program_subject хранятся предметы, которые нужны на определенное направление".

# Объяснение, предложенное Данил Дегтерев:
# "Если мы джойним enrollee_subject только по subject_id , то мы подсоединяем результаты всех людей, у которых они
# есть по этому предмету."


SELECT
    p.name_program,
    e.name_enrollee,
    SUM(es.result) AS itog
FROM
      program p
      JOIN program_enrollee pe USING (program_id)
      JOIN enrollee e USING (enrollee_id)
      JOIN enrollee_subject es USING (enrollee_id)
      JOIN program_subject ps USING (subject_id, program_id)
GROUP BY
     p.name_program,
     e.name_enrollee
ORDER BY
     p.name_program,
     itog DESC;




# Вывести название образовательной программы и фамилию тех абитуриентов, которые подавали документы на эту
# образовательную программу, но не могут быть зачислены на нее. Эти абитуриенты имеют результат по одному или
# нескольким предметам ЕГЭ, необходимым для поступления на эту образовательную программу, меньше минимального балла.
# Информацию вывести в отсортированном сначала по программам, а потом по фамилиям абитуриентов виде.

# Например, Баранов Павел по «Физике» набрал 41 балл, а  для образовательной программы «Прикладная механика»
# минимальный балл по этому предмету определен в 45 баллов. Следовательно, абитуриент на данную программу не может
# поступить

# Результат
#
# +-----------------------------+---------------+
# | name_program                | name_enrollee |
# +-----------------------------+---------------+
# | Мехатроника и робототехника | Баранов Павел |
# | Прикладная механика         | Баранов Павел |
# +-----------------------------+---------------+

# Для этого задания в базу данных добавлена строка:
# INSERT INTO enrollee_subject (enrollee_id, subject_id, result) VALUES (2, 3, 41);
# Добавлен человек, который сдавал Физику, но не подал документы ни на одну образовательную программу,
# где этот предмет нужен.

SELECT
    p.name_program,
    e.name_enrollee
FROM
      program p
      JOIN program_enrollee pe USING (program_id)
      JOIN enrollee e USING (enrollee_id)
      JOIN enrollee_subject es USING (enrollee_id)
      JOIN program_subject ps USING (subject_id, program_id)
GROUP BY
     name_program,
     name_enrollee
     HAVING SUM(result < min_result) > 0
ORDER BY
     name_program;

SELECT
    name_program,
    name_enrollee
FROM
    program p
     JOIN program_enrollee USING (program_id)
     JOIN enrollee e USING (enrollee_id)
     JOIN program_subject ps USING (program_id)
     JOIN enrollee_subject es ON
         (
           e.enrollee_id = es.enrollee_id AND
           ps.subject_id = es.subject_id AND
           result < min_result
         )
ORDER BY
    name_program;
