"""
Общественное питание 😥
Вам доступен файл food_services.json, содержащий список JSON-объектов,
которые представляют данные о заведениях общественного питания:

[
   {
      "Name": "СМЕТАНА",
      "IsNetObject": "нет",
      "OperatingCompany": "",
      "TypeObject": "кафе",
      "AdmArea": "Северо-Восточный административный округ",
      "District": "Ярославский район",
      "Address": "город Москва, улица Егора Абакумова, дом 9",
      "SeatsCount": 48
   },
   ...
]

Под «заведением» будем подразумевать один JSON-объект из этого списка. У заведения имеются следующие атрибуты:

    Name — название
    IsNetObject — да/нет в зависимости от того, является ли заведение сетевым
    OperatingCompany — название сети
    TypeObject — вид (кафе, столовая, ресторан и т.д.)
    AdmArea — административная зона District — район
    Address — полный адрес SeatsCount — количество мест

Напишите программу, которая:
    определяет район Москвы, в котором находится больше всего заведений, и выводит название этого района и количество
    заведений в нем определяет сеть с самым большим числом заведений и выводит название этой сети и количество
    заведений этой сети

Полученные значения программа должна вывести в следующем формате:
<район>: <количество заведений>
<название сети>: <количество заведений>

Примечание 1. Гарантируется, что искомая сеть единственная.
Примечание 2. Пример вывода:
район Метрогородок: 456
Французская пекарня SeDelice: 144

"""
# import pandas as pd
#
#
# def print_result(res: pd.DataFrame) -> str or None:
#     name = list(res.idxmax())[0]
#     count = list(res.max())[0]
#     return f'{name}: {count}'
#
#
# df = pd.read_json('food_services.json')
# result1 = df.groupby(['District']).agg(['count'])
# result2 = df[df['IsNetObject'] == 'да'].groupby(['OperatingCompany']).agg(['count'])
#
# print(print_result(result1))
# print(print_result(result2))


def print_result(res: dict) -> str or None:
    name, count = max(res.items(), key=lambda x: x[1])
    return f'{name}: {count}'


with open('food_services.json', encoding='utf-8') as f_in:
    data, res1, res2 = __import__('json').load(f_in), {}, {}
    for s in data:
        res1[s['District']] = res1.get(s['District'], 0) + 1
        if 'да' in s['IsNetObject']:
            res2[s['OperatingCompany']] = res2.get(s['OperatingCompany'], 0) + 1

print(print_result(res1))
print(print_result(res2))
