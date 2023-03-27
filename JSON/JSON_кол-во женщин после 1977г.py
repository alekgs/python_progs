"""
В json-файле содержится информация о нескольких групп людей, при этом у каждой группы есть свой идентификатор. 

Ваша задача скачать файлик и самостоятельно найти идентификатор группы, в которой находится самое большое количество 
женщин, рожденных после 1977 года.

В качестве ответа необходимо указать через пробел идентификатор найденной группы и сколько в ней было женщин,
рожденных после 1977 года.

"""
import json

with open('group_people.json') as f_json:
    data = json.load(f_json)

# Вариант 1
d = {sum(map(lambda x: 1 if (x['gender'] == 'Female' and x['year'] > 1977) else 0, m['people'])): m['id_group'] for m in data}
print(*max(d.items())[::-1])

# Вариант 2
# d = {m['id_group']: sum(map(lambda x: 1 if (x['gender'] == 'Female' and x['year'] > 1977) else 0, m['people'])) for m in data}
# print(fem_1977 := max(d, key=d.get), d[fem_1977])
