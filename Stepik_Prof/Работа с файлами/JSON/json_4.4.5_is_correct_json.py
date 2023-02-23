"""
Функция is_correct_json()

Реализуйте функцию is_correct_json(), которая принимает один аргумент:
    string — произвольная строка
Функция должна возвращать True, если строка string удовлетворяет формату JSON, или False в противном случае.

Примечание 1. Вспомните про конструкцию try-except из урока.

Sample Input 1:
data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))

Sample Output 1:
True

Sample Input 2:
print(is_correct_json('number = 17'))
Sample Output 2:
False
"""

import json


def is_correct_json(string: str) -> bool:
    """ Возвращает True, если строка string удовлетворяет формату JSON,
       или False в противном случае """
    try:
        json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


# data = "{'number': '17'}"
data = '{"age": 7}'
print(is_correct_json(data))
