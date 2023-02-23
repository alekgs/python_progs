"""
Популярные домены

Вам доступен файл data.csv, который содержит неповторяющиеся данные о пользователях некоторого ресурса.
В первом столбце записано имя пользователя, во втором — фамилия, в третьем — адрес электронной почты:

first_name,surname,email
John,Wilson,johnwilson@outlook.com
Mary,Wilson,marywilson@list.ru
...

Напишите программу, которая создает файл domain_usage.csv, имеющий следующее содержание:

domain,count
rambler.ru,24
iCloud.com,29
...

где в первом столбце записано название почтового домена, а во втором — количество пользователей, использующих данный
домен.
Домены в файле должны быть расположены в порядке возрастания количества их использований, при совпадении
количества использований — в лексикографическом порядке.

Примечание 1. Разделителем в файле data.csv является запятая, при этом кавычки не используются.
Примечание 2. Указанный файл доступен по ссылке. Ответ на задачу доступен по ссылке.
Примечание 3. Начальная часть файла domain_usage.csv выглядит так:

domain,count
rambler.ru,24
iCloud.com,29
...

Примечание 4. При открытии файла используйте явное указание кодировки UTF-8.

"""
import csv

with open('data.csv', encoding='utf-8') as f_in, \
     open('domain_usage.csv', 'w', encoding='utf-8', newline='') as f_out:

    rows, result = csv.DictReader(f_in, delimiter=','), {}

    for row in rows:
        domain = row['email'].split('@')[-1]
        result[domain] = result.get(domain, 0) + 1

    f_out.write(f'domain,count\n')

    for d in sorted(result, key=lambda k: (int(result[k]), k)):
        f_out.write(f'{d},{result[d]}\n')

