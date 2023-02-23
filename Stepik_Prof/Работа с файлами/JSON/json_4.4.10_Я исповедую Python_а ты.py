"""
Я исповедую Python, а ты?

Вам доступен файл countries.json, содержащий список JSON-объектов c информацией
о странах и исповедуемых в них религиях:
[
   {
      "country": "Afghanistan",
      "religion": "Islam"
   },
   {
      "country": "Albania",
      "religion": "Islam"
   },
   ...
]

Каждый объект из этого списка содержит два атрибута:

    country — страна
    religion — исповедуемая религия

Напишите программу, которая создает единственный JSON-объект, имеющий в качестве ключа название религии, а в качестве
значения — список стран, в которых исповедуется данная религия.
Полученный JSON-объект программа должна записать в файл religion.json.

Примечание 1. Страны в списках должны располагаться в своем исходном порядке.
Примечание 2. Начальная часть файла religion.json выглядит так:

{
   "Islam":[
      "Afghanistan",
      "Albania",
      "Algeria",
      ...
   ],
   ...
}
"""
import json

with open('countries.json', encoding='utf-8') as f_in, open('religion.json', 'w') as f_out:
    res = {}
    [res.setdefault(s['religion'], []).append(s['country']) for s in json.load(f_in)]
    json.dump(res, f_out, indent=3)
