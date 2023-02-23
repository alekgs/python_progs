"""
Восстановление недостающих ключей

Вам доступен файл people.json, содержащий список JSON-объектов.
Причем у различных объектов может быть различное количество ключей:

[
   {
      "age": 33,
      "country": "Lesotho",
      "phone": "(927) 316-2249",
      "family_status": "married",
      "email": "neonatus@outlook.com"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey",
      "children": "yes",
      "email": "ismail@gmail.com",
      "university": "Khalifa University",
      "family_status": "married"
   },
   ...
]

Напишите программу, которая добавляет в каждый JSON-объект из данного списка все недостающие ключи, присваивая этим
ключам значение null. Ключ считается недостающим, если он присутствует в каком-либо другом объекте, но отсутствует в
данном. Программа должна создать список с обновленными JSON-объектами и записать его в файл updated_people.json.

Примечание 1.
JSON-объекты в создаваемом программой списке должны располагаться в своем исходном порядке. Порядок
ключей в JSON-объектах не важен.

Примечание 2.
Например, если бы файл people.json имел вид:

[
   {
      "age": 33,
      "country": "Lesotho"
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]

то программа должна была создать файла updated_people.json со следующим содержанием:

[
   {
      "age": 33,
      "country": "Lesotho"
      "name": null
   },
   {
      "age": 25,
      "country": "Guinea",
      "name": "Dorey"
   }
]
"""
import json

with open('people.json', encoding='utf-8') as f_in, open('updated_people.json', 'w') as f_out:
    d = json.load(f_in)
    keys_set = set(key for s in d for key in s.keys())
    [s.update({k: None for k in s.keys() ^ keys_set}) for s in d]
    json.dump(d, f_out, indent=3)

# Решение № 2
# people = json.load(f_in)
# d = {k: None for i in people for k in i.keys()}
# json.dump([d | i for i in people], f_out, indent=3)

# Решение № 3
#  json.dump([dict.fromkeys(max(d, key=len)) | s for s in d], f_out, indent=3)

# Решение № 4 - Дмитрий Гудков
#     all_keys = max((data := json.load(f_in)), key=len).keys()
#     [i.setdefault(k, None) for i in data for k in all_keys]
#     json.dump(data, f_out, indent=3)
