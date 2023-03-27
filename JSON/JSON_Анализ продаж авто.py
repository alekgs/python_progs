"""
Анализ продаж

К вам в руки попал файлик формата json, в котором содержится информация одного автосалона о продажах менеджеров.
В файле указано для каждого менеджера список проданных им автомобилей, а также проставлена цена продажи каждого
автомобиля.

Ваша задача скачать файлик и самостоятельно найти самого успешного менеджера по итоговой сумме продаж.
В качестве ответа нужно через пробел указать сперва его имя, затем фамилию и после общую сумму его продаж.

"""
import json

with open('manager_sales.json') as f_json:
    data = json.load(f_json)

# Вариант 1 d = {f"{m['manager']['first_name']} {m['manager']['last_name']}": sum(map(lambda p: p['price'],
# m['cars'])) for m in data} print(number_one := max(d, key=d.get), d[number_one])

# вариант 2
# создаем словарь: ключ -> сумма продаж ['price']
d = {sum(map(lambda p: p['price'], m['cars'])): f"{m['manager']['first_name']} {m['manager']['last_name']}" for m in data}
print(*max(d.items())[::-1])



