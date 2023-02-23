"""
Разные типы

Вам доступен файл data.json, содержащий список различных объектов:

[
   "nwkWXma",
   null,
   {
      "ISgHT": "dIUbf"
   },
   "Pzt",
   "BXcbGVTE",
   ...
]

Напишите программу, которая создает список, элементами которого являются объекты из списка, содержащегося в файле
data.json, измененные по следующим правилам:

    если объект является строкой, в его конец добавляется восклицательный знак
    если объект является числом, он увеличивается на единицу
    если объект является логическое значением, он инвертируется
    если объект является списком, он удваивается
    если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
    если объект является пустым значением (null), он не добавляется

Полученный список программа должна записать в файл updated_data.json.

Примечание 1. Например, если бы файл data.json имел вид:

["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
то программа должна была бы создать файл updated_data.json со следующим содержанием:
["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

"""
import json

with open('data.json', encoding='utf-8') as f:
    result = []
    for s in json.load(f):
        if isinstance(s, str):
            result.append(f'{s}!')
        elif isinstance(s, bool):
            result.append((True, False)[s])
        elif isinstance(s, (int, float)):
            result.append(s + 1)
        elif isinstance(s, list):
            s.extend(s)
            result.append(s)
        elif isinstance(s, dict):
            s["newkey"] = None
            result.append(s)

with open('updated_data.json', 'w', encoding='utf-8') as f_out:
    json.dump(result, f_out, indent=3)

# import json
#
# with open('data.json', encoding='utf-8') as f, open('updated_data.json', 'w', encoding='utf-8') as f_out:
#     data = json.load(f)
#     conv_values = {
#         str: lambda x: x + '!',
#         int: lambda x: x + 1,
#         bool: lambda x: not x,
#         list: lambda x: x * 2,
#         dict: lambda x: {**x, "newkey": None},
#     }
#     result = []
#     for d in data:
#         if type(d) in conv_values:
#             result.append(conv_values[type(d)](d))
#     json.dump(result, f_out, indent=3)
